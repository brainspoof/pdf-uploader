from django.db import models

# Create your models here.

class PDF(models.Model):
    user_email = models.EmailField()
    secret = models.CharField(max_length=500)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return f'PDF of {self.user_email}.'
