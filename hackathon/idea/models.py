from django.db import models

# Create your models here.
class Testing_purpose(models.Model):
    name=models.CharField(max_length=50)
    college=models.CharField(max_length=50)
    
