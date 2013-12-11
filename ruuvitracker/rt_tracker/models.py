from django.db import models
from ruuvitracker.rt_user.models import User, Group


# Create your models here.
class Tracker(models.Model):
    owner = models.ForeignKey(User)
    groups = models.ManyToManyField(Group)
    tracker_code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    latest_activity = models.DateTimeField()
    shared_secret = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Session(models.Model):
    tracker = models.ForeignKey(Tracker)
    session_code = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Event(models.Model):
    sessions = models.ManyToManyField(Session)
    session_code = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Location(models.Model):
    tracker = models.ForeignKey(Tracker, empty=True)
    session = models.ForeignKey(Session, empty=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    horizontal_accuracy = models.FloatField()
    vertical_accuracy = models.FloatField()
    speed = models.DecimalField(max_digits=4, decimal_places=1)
    heading = models.DecimalField(max_digits=4, decimal_places=1)
    satellite_count = models.PositiveSmallIntegerField()
    altitude = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
