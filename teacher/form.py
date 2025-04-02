from django import forms

class TeachersForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"Enter Your Name", "class":"form-control"}) , min_length=5 , error_messages={'min_length':"Min Lenght of name should be  more than 5","required":"Name field cannot be empty"})
    email=forms.EmailField(label="Your Email"  , required=False , help_text="We accept email of google only" , widget=forms.EmailInput( attrs={ "class":"form-control","placeholder":"Enter Your Email Here"}))
    phone_number=forms.IntegerField(min_value=11, label="Your Phone Number ( +92 )", widget=forms.NumberInput(attrs={"class":"form-control" , 'placeholder':"Enter Your Phone Number"}))

    Bio=forms.CharField(widget=forms.Textarea(attrs={'cols':5,"placeholder":"Bio" , "class":"form-control"}))