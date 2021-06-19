from django.db import models

# Create your models here.

class csvs(models.Model):
    csv_file=models.FileField(upload_to='csvs', max_length=100)
    uploaded=models.DateTimeField(auto_now_add=True)
    activated=models.BooleanField(default=False)

   