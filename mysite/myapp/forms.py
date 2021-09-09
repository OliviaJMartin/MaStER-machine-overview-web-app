from django import forms

Status_Choices = [
    'Fully Serviceable',
    'Clinical With Limitations',
    'On Service/PMI',
    'Unserviceable'
]


class UpdateStatus(forms.Form):
    status = forms.CharField(label='EnterStatus',
                             widget=forms.Select(choices=Status_Choices))
    description = forms.CharField(max_length=150)
    comments = forms.CharField(max_length=255)
