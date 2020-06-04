from django.db import models

# Create your models here.

def get_path(instance, filename):
    return f'pdfs/{instance.user_email}/{filename}'

class PDF(models.Model):
    user_email = models.EmailField()
    secret = models.CharField(max_length=500)
    pdf = models.FileField(upload_to=get_path)

    def __str__(self):
        return f'PDF of {self.user_email}.'
