from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


"""
class Clientes:
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dni = models.CharField(max_length=10)
    email = models.EmailField()
"""
