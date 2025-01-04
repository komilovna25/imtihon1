from django.db import models
from ckeditor.fields import RichTextField
from hitcount.models import HitCountMixin,HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django import forms

class Category(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.name
    
class Portfolio(models.Model):
    image = models.ImageField(upload_to='Images/portfolio', max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description[:50]  
    
class About(models.Model):
    image = models.ImageField(upload_to='Images/about', max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.image.name if self.image else 'No image'


class Contact(models.Model):
    name = models.CharField(max_length=100)  
    email = models.EmailField()
    message = models.TextField()
   
    def __str__(self):
        return f"{self.name} {self.email}" 
    
class Services(models.Model):
        title = models.CharField(max_length=70)
        description = models.TextField()
        created_date = models.DateTimeField(auto_now_add=True)
    
        def __str__(self):
             return self.description[:50]  
    
