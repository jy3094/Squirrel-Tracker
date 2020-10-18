from django.forms import ModelForm
from .models import Squirrel

class Form(ModelForm):
    class Meta:
        model = Squirrels
        fields = '__all__'
