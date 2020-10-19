import csv
import datetime
from django.core.management.base import BaseCommand
from sightings.models import Squirrel
class Command(BaseCommand):
    help = 'Import squirrels information into database'
    
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
        
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        
        try:
            with open(path, encoding = 'utf-8') as f:
                reader = csv.DictReader(f)
                for x in reader:
                    squirrel = Squirrel(
                            X = x['X'],
                            Y = x['Y'],
                            Squirrel_ID = x['Unique Squirrel ID'],
                            Shift = x['Shift'],
                            Date = datetime.date(int(x['Date'][-4:]), int(x['Date'][:2]), int(x['Date'][2:4])),
                            Age = x['Age'],
                            Primary_Fur_Color = x['Primary Fur Color'],
                            Location = x['Location'],
                            Specific_Location = x['Specific Location'],
                            Running = True if x['Running']=='True' else False,
                            Chasing = True if x['Chasing']=='True' else False,
                            Climbing = True if x['Climbing']=='True' else False,
                            Eating = True if x['Eating']=='True' else False,
                            Foraging = True if x['Foraging']=='True' else False,
                            Other_Activities = x['Other Activities'],
                            Kuks = True if x['Kuks']=='True' else False,
                            Quaas = True if x['Quaas']=='True' else False,
                            Moans = True if x['Moans']=='True' else False,
                            Tail_Flags = True if x['Tail flags']=='True' else False,
                            Tail_Twitches = True if x['Tail twitches']=='True' else False,
                            Approaches = True if x['Approaches']=='True' else False,
                            Indifferent = True if x['Indifferent']=='True' else False,
                            Runs_From = True if x['Runs from']=='True' else False,
                    )
                    squirrel.save
        except csv.Error as e:
            pring(f'An error has occured at {reader.line_num}')
