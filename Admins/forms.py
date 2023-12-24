from django import forms

from .models import Team


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