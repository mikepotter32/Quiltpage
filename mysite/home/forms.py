from django import forms

from .models import Quilt

class QuiltForm(forms.ModelForm):
    class Meta:
        model = Quilt
        exclude = [
            'cost',
            'quiltID',
            'pic',
        ]
