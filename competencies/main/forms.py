from django.forms import ModelForm, TextInput, FileInput, Select, ClearableFileInput, FileField, Textarea, NumberInput
from django import forms
from .models import *


class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ["surname", "name", "middleName", "structuralDivision", "department", "heldPost"]
        widgets = {
            "surname": TextInput(
                attrs={"class": "form-control"}
            ),
            "name": TextInput(
                attrs={"class": "form-control"}
            ),
            "middleName": TextInput(
                attrs={"class": "form-control"}
            ),
            "structuralDivision": TextInput(
                attrs={"class": "form-control"}
            ),
            "department": TextInput(
                attrs={"class": "form-control"}
            ),
            "heldPost": TextInput(
                attrs={"class": "form-control"}
            )
        }
