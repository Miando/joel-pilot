from django import forms
from .models import PersonOptions, User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'email']


class IsActiveForm(forms.ModelForm):

    class Meta:
        model = PersonOptions
        fields = ('is_active', )


class OptionsForm(forms.ModelForm):

    class Meta:
        model = PersonOptions
        fields = ('job_name', 'city', 'category', 'subcategory', 'keyword', 'stop_word', 'is_active')


class EditOption(forms.Form):
    pk = forms.CharField(max_length=100, required=False)
    is_active = forms.BooleanField(required=False)


class NewTask(forms.Form):
    category = forms.CharField(max_length=100, required=False)
    village = forms.CharField(max_length=1000, required=False)
    subcategory = forms.CharField(max_length=100, required=False)
    keyword = forms.CharField(max_length=100, required=False)
    stop_word = forms.CharField(max_length=100, required=False)
    url1 = forms.CharField(max_length=1000, required=False)
    job_name = forms.CharField(max_length=100,)
    is_active = forms.BooleanField(initial=True, required=False)
    option1 = forms.CharField(max_length=1000, required=False)
    option2 = forms.CharField(max_length=1000, required=False)
    option3 = forms.CharField(max_length=1000, required=False)
    option4 = forms.CharField(max_length=1000, required=False)
    option5 = forms.CharField(max_length=1000, required=False)
    option6 = forms.CharField(max_length=1000, required=False)
    option7 = forms.CharField(max_length=1000, required=False)
    option8 = forms.CharField(max_length=1000, required=False)
    option9 = forms.CharField(max_length=1000, required=False)
    option10 = forms.CharField(max_length=1000, required=False)
    option11 = forms.CharField(max_length=1000, required=False)
    option12 = forms.CharField(max_length=1000, required=False)
    option13 = forms.CharField(max_length=1000, required=False)
    option14 = forms.CharField(max_length=1000, required=False)
    option15 = forms.CharField(max_length=1000, required=False)
    option16 = forms.CharField(max_length=1000, required=False)
    option17 = forms.CharField(max_length=1000, required=False)
    option18 = forms.CharField(max_length=1000, required=False)
    option19 = forms.CharField(max_length=1000, required=False)
    option20 = forms.CharField(max_length=1000, required=False)
    option21 = forms.CharField(max_length=1000, required=False)
    option22 = forms.CharField(max_length=1000, required=False)
    option23 = forms.CharField(max_length=1000, required=False)
    option24 = forms.CharField(max_length=1000, required=False)
    option25 = forms.CharField(max_length=1000, required=False)
    option26 = forms.CharField(max_length=1000, required=False)
    option27 = forms.CharField(max_length=1000, required=False)
    option28 = forms.CharField(max_length=1000, required=False)
    option29 = forms.CharField(max_length=1000, required=False)
    option30 = forms.CharField(max_length=1000, required=False)
    option31 = forms.CharField(max_length=1000, required=False)
    option32 = forms.CharField(max_length=1000, required=False)
    option33 = forms.CharField(max_length=1000, required=False)
    option34 = forms.CharField(max_length=1000, required=False)
    option35 = forms.CharField(max_length=1000, required=False)
    option36 = forms.CharField(max_length=1000, required=False)
    option37 = forms.CharField(max_length=1000, required=False)
    option38 = forms.CharField(max_length=1000, required=False)
    option39 = forms.CharField(max_length=1000, required=False)
    option40 = forms.CharField(max_length=1000, required=False)
    option41 = forms.CharField(max_length=1000, required=False)
    option42 = forms.CharField(max_length=1000, required=False)
    option43 = forms.CharField(max_length=1000, required=False)
    option44 = forms.CharField(max_length=1000, required=False)
    option45 = forms.CharField(max_length=1000, required=False)
    option46 = forms.CharField(max_length=1000, required=False)
    option47 = forms.CharField(max_length=1000, required=False)
    option48 = forms.CharField(max_length=1000, required=False)
    option49 = forms.CharField(max_length=1000, required=False)
    option50 = forms.CharField(max_length=1000, required=False)
