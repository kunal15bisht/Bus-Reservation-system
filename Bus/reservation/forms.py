from django import forms
from reservation.models import User
class Userform(forms.ModelForm):
    class Meta:
        model = User
        fileds = ["username","mail", "password"]