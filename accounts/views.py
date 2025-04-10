from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import RegistartionForm

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
    if request.method == 'POST':
        form=AuthenticationForm(request=request,data=request.POST)

        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data["password"]
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                home = reverse("home")
                return HttpResponseRedirect(home)
    else:
        form=AuthenticationForm()
    context={"form":form}
    return render(request,"accounts/login.html",context)
