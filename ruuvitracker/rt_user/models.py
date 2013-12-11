from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Group(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User)
    members = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
