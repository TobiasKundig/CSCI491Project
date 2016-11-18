from django import forms
from django.forms import ModelForm
from .models import *

class PortfolioForm(forms.ModelForm):

    class Meta:
        model = Portfolio
        fields = ('name', 'header', 'style', 'img')

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('name', 'description', 'startdate', 'enddate')
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
            'startdate': forms.DateInput(attrs={'class': 'datepicker'}),
            'enddate': forms.DateInput(attrs={'class': 'datepicker'})
        }



