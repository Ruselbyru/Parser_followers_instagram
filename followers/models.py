from django.db import models
from django.urls import reverse

# Create your models here.

class Profile (models.Model):
    name = models.CharField(max_length=100 , verbose_name='Имя профиля')
    download = models.BooleanField(null=False, default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse ('home')


class Followers (models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=False,default=None)
    followers = models.CharField(max_length=100)

    def __str__(self):
        return self.followers


class Files(models.Model):
    adminupload = models.FileField(upload_to='media')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title