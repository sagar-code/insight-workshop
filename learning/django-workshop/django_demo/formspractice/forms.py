from django import forms
from .models import FormsModel

class MyForm(forms.Form):
    name = forms.CharField(max_length=30)
    age = forms.IntegerField()

    def clean_name(self):
        print(f"self.cleaned_data: {self.cleaned_data}")
        name = self.cleaned_data['name']
        # i can do some validations or clean the name
        return name.lower()


# model forms
class FormsModelForm(forms.ModelForm):
    class Meta:
        model = FormsModel
        fields = ['name', 'email']
