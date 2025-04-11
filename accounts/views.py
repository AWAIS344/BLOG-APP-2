from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import RegistartionForm,LoginFrom

# Create your views here.

def register(request):
    if request.method == 'POST':
        form=RegistartionForm(request.POST)
        if form.is_valid():
            form.save()

            home = reverse("home")

            return HttpResponseRedirect(home)
    else:
        form=RegistartionForm()
    context={"form":form}
    return render(request,"accounts/home.html",context)

def auth_login(request):
    home = reverse("home")
    if request.user.is_authenticated:
        return HttpResponseRedirect(home)
    else:

        if request.method == 'POST':
            form=LoginFrom(request=request,data=request.POST)

            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data["password"]
                user=authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    
                    return HttpResponseRedirect(home)
        else:
            form=LoginFrom()
        context={"form":form}
        return render(request,"accounts/login.html",context)

