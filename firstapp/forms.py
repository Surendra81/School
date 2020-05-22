from django import forms
from .models import School 

class CreateSchool(forms.ModelForm):
    class meta:
        model = School
        fields = '__all__'
        