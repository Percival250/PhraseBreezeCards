from django import forms
from . import models
import main_app.models


class CopySetForm(forms.ModelForm):

    class Meta:
        model = main_app.models.Set
        fields = ['name']
class ChooseCategoryForm(forms.ModelForm):
    name = forms.CharField(
        label='Search',
        required=False
    )

    class Meta:
        model = models.Set
        fields = ['name', 'category']
