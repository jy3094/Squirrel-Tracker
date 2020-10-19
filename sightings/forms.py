from django.forms import ModelForm

from .models import Squirrel


class Form(ModelForm):
    class Meta:
        model = Squirrel
        fields = ['X', 'Y', 'Shift', 'Date', 'Age']


class CreateForm(ModelForm):
    class Meta:
        model = Squirrel
        fields = ['X', 'Y', 'Squirrel_ID',
                  'Shift', 'Date', 'Age',
                  'Primary_Fur_Color', 'Location', 'Specific_Location',
                  'Running', 'Chasing', 'Climbing',
                  'Eating', 'Foraging', 'Other_Activities',
                  'Kuks', 'Quaas', 'Moans',
                  'Tail_Flags', 'Tail_Twitches', 'Approaches',
                  'Indifferent', 'Runs_From']
