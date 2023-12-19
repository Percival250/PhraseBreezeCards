from django import forms
import community_library.models
from . import models


class SetForm(forms.ModelForm):

    class Meta:
         model = models.Set
         fields = ['name']


class SetExistsForm(forms.Form):

    name = forms.CharField(
        max_length=250,
        label='Name',
        help_text='Set with this name already exists!'
    )


class CardForm(forms.ModelForm):

    front_side = forms.CharField(
        max_length=250,
        label='Front side',
    )
    back_side = forms.CharField(
        max_length=250,
        label='Back side',
    )

    class Meta:
        model = models.Card
        fields = ['front_side', 'back_side', 'create_reverse_card']


class EditCardForm(forms.ModelForm):
    class Meta:
        model = models.Card
        fields = ['front_side', 'back_side']


class ShareSetForm(forms.ModelForm):

    class Meta:
        model = community_library.models.Set
        fields = ['name']