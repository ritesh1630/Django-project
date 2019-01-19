from django import forms
from django.core import validators
from django.contrib.auth.models import User
from . import models

def start_with_R(value):
    if value[0]!="R":
        raise forms.ValidationError("Enter the name that start with R")

class CustForm(forms.Form):
    Custname=forms.CharField(label="Customer Name",validators=[start_with_R])
    Custsal = forms.FloatField(label="Customer Sal")
    Custadd = forms.CharField(widget=forms.Textarea,label="Customer Address",validators=[validators.MaxLengthValidator(10)])

    def clean_Empname(self):
        input=self.cleaned_data["Custname"]
        if len(input)<4:
            raise forms.ValidationError("Enter string greater than 4 --Ritesh")
        return input


class EmpForm(forms.ModelForm):
    class Meta:
        model=models.Employee
        fields="__all__"

class Sign_Up_Form(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password","email","first_name","last_name"]