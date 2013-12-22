from django.db import models


class SensorData(models.Model):
    timestamp = models.DateTimeField()
    signal = models.SmallIntegerField()
    door_open = models.NullBooleanField()
    motion_sensed = models.NullBooleanField()