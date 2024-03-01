from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length= 200)
    content = models.TextField()
    short_description = models.CharField(max_length=300, default="")
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
class Contact(models.Model):
    name = models.CharField(max_length= 25)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    desc = models.TextField()


def __str__(self):
    return self.title