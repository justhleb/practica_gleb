from django import forms
from .models import Image


class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={"class": "input_file"}))
    class Meta:
        model = Image
        fields = ('image',)


class CheckboxForm(forms.Form):
    sea = forms.BooleanField(label='море', required=False)
    city = forms.BooleanField(label='город', required=False)
    forest = forms.BooleanField(label='лес', required=False)
    field = forms.BooleanField(label='поле', required=False)

    cat = forms.BooleanField(label='кот', required=False)
    home = forms.BooleanField(label='дом', required=False)
    chair = forms.BooleanField(label='стул', required=False)
    table = forms.BooleanField(label='стол', required=False)
