from django import forms
from .models import FieldsModel


class FieldsForm(forms.ModelForm):
    field_name_uz=forms.CharField()
    field_name_en=forms.CharField()
    field_name_ru=forms.CharField()

    field_adress_uz=forms.CharField()
    field_adress_en=forms.CharField()
    field_adress_ru=forms.CharField()    

    class Meta:
        model=FieldsModel
        exclude=('field_name', 'field_adress')