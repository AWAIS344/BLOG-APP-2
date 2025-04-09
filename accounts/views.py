from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.data)
        if form.is_valid():
            form.save()

            home = reverse("home")

            return HttpResponseRedirect(home)
    else:
        form=UserCreationForm()
    context={"form":form}
    return render(request,"accounts/home.html",context)
