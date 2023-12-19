from django import forms
from . import models
import main_app.models


class CopySetForm(forms.ModelForm):

    class Meta:
        model = main_app.models.Set
        fields = ['name']
