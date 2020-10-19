import csv

from django.core.management.base import BaseCommand

from sightings.models import Squirrel

class Command(BaseCommand):
    help = "Output the data into a csv file"

    def add_arguments(self, parser):
        parser.add_argument('args', type = str, nargs='*')

    def handle(self, *args, **kwargs):
        path = args[0]
        fields = Squirrel._meta.fields
        with open(path,'w') as f:
            record = csv.writer(f)
            for item in Squirrel.objects.all():
                row = [getattr(item,field.name) for field in fields]
                record.writerow(row)
            f.close()

