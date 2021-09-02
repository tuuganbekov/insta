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
