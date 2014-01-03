from datetime import datetime
import logging
from django.db import models
from pytz import timezone


logger = logging.getLogger(__name__)


class SensorData(models.Model):
    timestamp = models.DateTimeField()
    signal = models.SmallIntegerField()
    door_open = models.NullBooleanField()
    motion_sensed = models.NullBooleanField()

    class Meta:
        unique_together = ('timestamp', 'signal', 'door_open', 'motion_sensed')

    @classmethod
    def create_from_string(cls, string):
        row = string.split(',')
        return cls.create_from_csv_row(row)

    @classmethod
    def create_from_csv_row(cls, row):
        timestamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')

        timestamp = timestamp.replace(tzinfo=timezone('US/Pacific'))
        signal = int(row[1])
        door_open = row[2] == 'D1'
        motion_sensed = row[3] == 'M1'

        logger.debug(timestamp, signal, door_open, motion_sensed)

        # build db object
        s = SensorData(timestamp=timestamp,
                       signal=signal,
                       door_open=door_open,
                       motion_sensed=motion_sensed)
        return s

    def __unicode__(self):
        return '%s, Door Open: %s, Motion Sensed: %s' % (self.timestamp,
                                                         self.door_open,
                                                         self.motion_sensed)