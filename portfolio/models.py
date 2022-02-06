from tabnanny import verbose
from django.db import models

# Create your models here.

class About(models.Model):
    age = models.IntegerField(blank=True, null=True)
    residence = models.CharField(max_length=255, blank=True, null=True)
    adress = models.TextField(max_length=255, null=True,blank=True)
    email = models.EmailField(max_length=255)
    phone = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return 'About Myself'
    
    class Meta:
        verbose_name = 'About Myself'
        
        
class Testimonials(models.Model):
    comment = models.TextField(blank=True,null=True)
    writer_img = models.ImageField(upload_to='testimonials/')
    writer_name = models.CharField(max_length=127, null=True,blank=True)
    writer_position = models.CharField(max_length=127, null=True,blank=True)
    
    def __str__(self):
        return self.writer_name

    
