from django import forms
from .models import Curdoperations

class curdforms(forms.ModelForm):
    class Meta:
        model = Curdoperations
        fields = ['name','age','gender','email']

