from django import forms
from .models import Profile


class SearchForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
            attrs={"placeholder":"Введите имя"}))


class ProfileModelForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["name", "sur_name"]
# class NewForm(forms.Form):


class NewSearch(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"enter your name or surname"}))

    choisces = (
        ('first_name', 'filter by first name'),
        ('last_name', 'filter by first last_name')

    )
    a