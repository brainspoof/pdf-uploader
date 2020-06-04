from django import forms
from .models import PDF

class UploadPDF(forms.Form):
    user_email = forms.EmailField()
    secret = forms.CharField(widget=forms.PasswordInput)
    pdf = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = PDF
        fields = ['user_email', 'secret', 'pdf']

class SearchForm(forms.Form):
    user_email = forms.EmailField()
    secret = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        fields = ['user_email', 'secret']
