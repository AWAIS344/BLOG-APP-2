from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
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
