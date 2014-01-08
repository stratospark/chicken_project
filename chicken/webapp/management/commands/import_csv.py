import logging
from csv import reader

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from webapp.models import SensorData


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    args = '<file_path>'
    help = "Import SensorData from a specified log file"

    def handle(self, *args, **options):
        # TODO: don't hardcode path, load from relative path? or env variable?
        if len(args) > 0:
            file_path = args[0]
        else:
            file_path = '../chickens.txt'
        chicken_file = open(file_path)
        csv_reader = reader(chicken_file)
        for i, row in enumerate(csv_reader):
            s = SensorData.create_from_csv_row(row)

            try:
                s.save()
            except IntegrityError as e:
                logger.warning('Skipping %s, %s' % (row, e))

            if i % 100 == 0:
                logger.info('Total Imported: %d' % i)