from django import forms

class TeachersForm(forms.Form):
    name = forms.CharField(max_length=50)
    email=forms.EmailField(label="Your Email" , label_suffix=" = " , required=False)
    phone_number=forms.IntegerField(min_value=11, label="Your Phone Number ( +92 )")