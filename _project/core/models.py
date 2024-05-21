from django.db import models
from datetime import timedelta

# Create your models here.
class Activity(models.Model):
    name=models.TextField()

    def time_spent(self):
        delta = timedelta()
        for timelog in self.timelog_set.all():
            delta += (timelog.end_time - timelog.start_time)
        return str(delta)

class TimeLog(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    activity=models.ForeignKey("Activity",on_delete=models.CASCADE, null=True)

    def time_spent(self):
        time_difference = self.end_time - self.start_time
        days, seconds = divmod(time_difference.total_seconds(), 86400)  # 1 day = 86400 seconds
        hours, seconds = divmod(seconds, 3600)  # 1 hour = 3600 seconds
        minutes, seconds = divmod(seconds, 60)
        return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes"

