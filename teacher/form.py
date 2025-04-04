from django import forms
from .models import Teacher


# def start_s(value):
     
#     if value[0] != 'S' and value[0] != 's':
#         raise forms.ValidationError( f"The {value} should start with S or s")


class TeachersForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ['name','email',"phone_number",'bio']
        labels ={
            "name":"Your Name",
            "bio":"Write About Youself"
        }

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "phone_number":forms.NumberInput(attrs={"class":"form-control"}),
            "bio":forms.Textarea(attrs={"class":"form-control"}),
        }

        help_texts={
            "email":"We only Accept gmails",
        }
        
    # name = forms.CharField( widget=forms.TextInput(attrs={'placeholder':"Enter Your Name", "class":"form-control"}) , min_length=5 , error_messages={'min_length':"Min Lenght of name should be  more than 5","required":"Name field cannot be empty"})
    # email=forms.EmailField(label="Your Email"  , required=False , help_text="We accept email of google only" , widget=forms.EmailInput( attrs={ "class":"form-control","placeholder":"Enter Your Email Here"}))
    # phone_number=forms.IntegerField(min_value=11, label="Your Phone Number ( +92 )", widget=forms.NumberInput(attrs={"class":"form-control" , 'placeholder':"Enter Your Phone Number"}))

    # Bio=forms.CharField(widget=forms.Textarea(attrs={'cols':5,"placeholder":"Bio" , "class":"form-control"}))

    # def clean(self):
    #     cleaned_data=super().clean()
    #     name=self.cleaned_data['name']
    #     email=self.cleaned_data['email']

    #     if name[0] != 's' and name[0] != "S" :
    #         raise forms.ValidationError("The name should start with S or s")
        
    #     if email[0] != 's' and email[0] != "S" :
    #         raise forms.ValidationError("The Email should start with S or s")