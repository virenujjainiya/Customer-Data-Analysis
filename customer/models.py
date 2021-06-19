from django.db import models

# Create your models here.
class Customer(models.Model):
    company_name=models.CharField(max_length=50)
    budget=models.PositiveIntegerField()
    employment=models.PositiveIntegerField()
    joined_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.company_name)
    
