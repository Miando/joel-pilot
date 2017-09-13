from django import forms
from .models import PersonOptions


class OptionsForm(forms.ModelForm):

    class Meta:
        model = PersonOptions
        fields = ('job_name', 'city', 'category', 'subcategory', 'keyword', 'stop_word', 'is_active')