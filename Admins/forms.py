from typing import Any

from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q

from .models import Personel, Team


class TeamForm(forms.ModelForm):
    
    class Meta:
        model = Team
        fields = [
            'Access',
            'parent',
            'Name',
            'Description',
        ]
        widgets = {
            "Name": forms.TextInput(attrs={"class": "form-control", "required": "true"}),
            "Description": forms.Textarea(attrs={"class": "form-control", "required": "true"}),
        }

class PersonelForm(forms.ModelForm):

    class Meta:

        model = Personel
        fields = [
            'first_name',
            'last_name',
            'Phone',
            'NationalID',
            'JobTitle',
            'Team',
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "required": "true"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "required": "true"}),
            "Phone": forms.TextInput(attrs={"class": "form-control num-input", "required": "true"}),
            "NationalID": forms.TextInput(attrs={"class": "form-control num-input", "required": "true"}),
            "JobTitle": forms.TextInput(attrs={"class": "form-control", "required": "true"}),
            "Description": forms.Textarea(attrs={"class": "form-control", "required": "true"}),
        }
    def clean(self):
        cleaned_data = super().clean()
        Phone = cleaned_data["Phone"]
        NationalID = cleaned_data["NationalID"]
        try:
            PE = Personel.objects.get(Q(Phone=Phone) | Q(NationalID=NationalID))
            print(PE)
            # return False
            raise ValidationError('کاربر دیگری با این شماره تماس یا کد ملی موجود است')
        except:
            return super().clean()

    