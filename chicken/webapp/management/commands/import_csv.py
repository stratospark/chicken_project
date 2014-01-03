from datetime import datetime
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from csv import reader
from pytz import timezone

from webapp.models import SensorData


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        # TODO: don't hardcode path, load from relative path? or env variable?
        chicken_file = open('/Users/patr/PycharmProjects/chicken_project/chickens.txt')
        csv_reader = reader(chicken_file)
        for i, row in enumerate(csv_reader):
            s = SensorData.create_from_csv_row(row)

            try:
                s.save()
            except IntegrityError as e:
                print 'Skipping %s' % row
                print e


            if i % 100 == 0:
                print 'Total Imported: %d' % i