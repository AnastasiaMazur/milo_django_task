from django import forms
from .models import User

BIRTH_YEAR_CHOICES = range(1950, 2017)


class UserForm(forms.ModelForm):
    birthday = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

    class Meta:
        model = User
        fields = ('username', 'birthday', 'number',)
