from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from .models import DateModel

class DateForm(forms.ModelForm):
    class Meta:
        model = DateModel
        fields = ('date_field',)
        widgets = {
            'date_field': AdminDateWidget(),
        }