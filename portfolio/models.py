from tabnanny import verbose
from django.db import models

# Create your models here.

class About(models.Model):
    age = models.IntegerField(blank=True, null=True)
    residence = models.CharField(max_length=255, blank=True, null=True)
    adress = models.TextField(max_length=255, null=True,blank=True)
    email = models.EmailField(max_length=255)
    phone = models.TextField(null=True, blank=True)
    
    class Meta:
        verbose_name = 'About Myself'

    
