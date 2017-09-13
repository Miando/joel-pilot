from django import forms
from .models import PersonOptions


class OptionsForm(forms.ModelForm):

    class Meta:
        model = PersonOptions
        fields = ('job_name', 'city', 'category', 'subcategory', 'keyword', 'stop_word', 'is_active')


class NewTask(forms.Form):
    category = forms.CharField(max_length=100, required=False)
    subcategory = forms.CharField(max_length=100, required=False)
    option1 = forms.CharField(max_length=1000, required=False)
    option2 = forms.CharField(max_length=1000, required=False)
    option3 = forms.CharField(max_length=1000, required=False)
    option4 = forms.CharField(max_length=1000, required=False)

    # def extra_answers(self):
    #     for name, value in self.cleaned_data.items():
    #         if name.startswith('custom_'):
    #             yield (self.fields[name].label, value)
    #
    # def __init__(self, *args, **kwargs):
    #     extra = kwargs.pop('extra')
    #     super(NewTask, self).__init__(*args, **kwargs)
    #
    #     for i, question in enumerate(extra):
    #         self.fields['custom_%s' % i] = forms.CharField(max_length=100, label=question)
