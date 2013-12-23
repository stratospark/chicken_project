from datetime import datetime
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from csv import reader
from pytz import timezone

from webapp.models import SensorData


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        chicken_file = open('/Users/patr/PycharmProjects/chicken_project/chickens.txt')
        csv_reader = reader(chicken_file)
        for i, row in enumerate(csv_reader):
            # parse row data
            timestamp = datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S')
            timestamp = timestamp.replace(tzinfo=timezone('US/Pacific'))
            signal = int(row[1])
            door_open = row[2] == 'D1'
            motion_sensed = row[3] == 'M1'

            #print timestamp, signal, door_open, motion_sensed

            # build db object
            s = SensorData(timestamp=timestamp,
                           signal=signal,
                           door_open=door_open,
                           motion_sensed=motion_sensed)

            try:
                s.save()
            except IntegrityError as e:
                print 'Skipping %s' % row
                print e


            if i % 100 == 0:
                print 'Total Imported: %d' % i
