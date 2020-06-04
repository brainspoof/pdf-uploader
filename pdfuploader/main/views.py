from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadPDF, SearchForm
from .models import PDF
import hashlib
from django.contrib import messages

def strHash(secret):
    return hashlib.sha512(secret.encode()).hexdigest()

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = UploadPDF(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['user_email']
            files = request.FILES.getlist('pdf')
            secret = strHash(form.cleaned_data['secret'])
            success = 0
            fail = 0
            if len(files) >= 5:
                messages.error(request, 'You can only upload 5 or less PDFs at a time.')
                return render(request, 'main/index.html', {'form': form})
            for f in files:
                if f.name.endswith('.pdf'):
                    pdf = PDF(user_email=email, secret=secret, pdf=f)
                    pdf.save()
                    success += 1
                else:
                    fail += 1

            if success == len(files):
                messages.success(request, 'All files have been uploaded securely and successfully.')
            else:
                messages.warning(request, f'{fail} {"files" if fail > 1 else "fail"} can not be Uploaded.')
            return render(request, 'main/stats.html', {'success':success, 'fail':fail})
        else:
            return HttpResponse('Oops! Something went wrong.')
    return render(request, 'main/index.html', {'form': UploadPDF})


def search(request):
    pdfs = ''
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['user_email']
            secret = strHash(form.cleaned_data['secret'])
            pdfs = PDF.objects.filter(user_email=email, secret=secret)
            if len(pdfs) == 0:
                messages.error(request, 'No Files Found with those credentials.')
    return render(request, 'main/search.html', {'form': SearchForm, 'pdfs':pdfs})
