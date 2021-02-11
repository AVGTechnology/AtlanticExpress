from django import forms

from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LocationUpdateForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ["point", "Location"]


class ClientBillForm(forms.ModelForm):
    class Meta:
        model = BillClient
        fields = ["account", "bill_dis", "Amount"]
