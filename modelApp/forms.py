from django import forms
from modelApp.models import Persona

class PersonaRegistrationForm(forms.Form):
    nombre = forms.CharField()
    email = forms.CharField()
    telefono = forms.CharField()

class PersonaRegistrationForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'