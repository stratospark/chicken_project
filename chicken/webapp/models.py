from django.db import models


class SensorData(models.Model):
    timestamp = models.DateTimeField()
    signal = models.SmallIntegerField()
    door_open = models.NullBooleanField()
    motion_sensed = models.NullBooleanField()

    class Meta:
        unique_together = ('timestamp', 'signal', 'door_open', 'motion_sensed')

    def __unicode__(self):
        return '%s, Door Open: %s, Motion Sensed: %s' % (self.timestamp,
                                                         self.door_open,
                                                         self.motion_sensed)