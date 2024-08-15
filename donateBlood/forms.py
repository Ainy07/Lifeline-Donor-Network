from django import forms
from django.db.models import fields
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import *

class donorForm(ModelForm):
    
    class Meta:
        model = donor
        fields = ['Name','Phone','Email','Address','BloodType', 'age','medical_ailments']
    
