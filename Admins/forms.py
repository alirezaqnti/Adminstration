from django import forms

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
            'Address',
            'Team',
            'Status',
        ]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "required": "true"}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "required": "true"}),
            "Phone": forms.TextInput(attrs={"class": "form-control num-input", "required": "true"}),
            "NationalID": forms.TextInput(attrs={"class": "form-control num-input", "required": "true"}),
            "JobTitle": forms.TextInput(attrs={"class": "form-control", "required": "true"}),
            "Description": forms.Textarea(attrs={"class": "form-control", "required": "true"}),
        }
