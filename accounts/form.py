from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegistartionForm(UserCreationForm):

    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder":"e.g Awais"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"e.g Ali"}))
    Email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"xyz123@gmail.com"}))

    class Meta:
        model = User
        fields = ["username","first_name",]
        widgets={
            "username":forms.TextInput(attrs={"placeholder":"e.g awais8900" , "class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"placeholder":"e.g awais8900" , "class":"form-control"}),
            "password2":forms.PasswordInput(attrs={"placeholder":"e.g awais8900" , "class":"form-control"}),

        }
