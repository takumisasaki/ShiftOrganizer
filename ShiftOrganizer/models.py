from django.db import models

# Create your models here.
class Schedule(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    class Meta:
        app_label = 'ShiftOrganizer'