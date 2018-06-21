#import inbuilt forms
from django.forms import ModelForm, TextInput
#import model from models.py file
from .models import City 

class CityForm(ModelForm):
    class Meta:
        model = City 
        #only one field we want to use
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}