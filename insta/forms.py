from django import forms


class MyForm(forms.Form):
    title = forms.CharField(max_length=255, label="Vvedite title" ,
                            widget=forms.TextInput(
                                attrs={'placeholder':"Vvedite dannye"})
                            )
    descr = forms.CharField(max_length=255)

    def clean(self):
        title = self.cleaned_data['title']
        if len(title)<3:
            raise forms.ValidationError("слишком маленький тайтл")
        return self.cleaned_data