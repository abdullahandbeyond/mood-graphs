from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date, timedelta

# Create your models here.
class Mood(models.Model):
    name = models.CharField(default='Mood One', max_length=50)
    border = models.CharField(default='Colour One', max_length=50)
    background = models.CharField(default='Colour One', max_length=50)

    def __unicode__(self):
        return self.name
    def __repr__(self):
        return self.name
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Mood"

class Tracking(models.Model):
    mood = models.ForeignKey(Mood, default=None, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=None, blank=True, null=True, on_delete=models.CASCADE)
    workDate = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.mood} - {self.workDate}"

    class Meta:
        db_table = "Tracking"
