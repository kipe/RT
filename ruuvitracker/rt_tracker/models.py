from django.db import models
from ruuvitracker.rt_user.models import User, Group


# Create your models here.
class Tracker(models.Model):
    owner = models.ForeignKey(User)
    groups = models.ManyToManyField(Group)
    tracker_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
