from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class GenerateRandomMachineForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)]
    )