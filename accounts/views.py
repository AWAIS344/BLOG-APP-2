from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

# Create your views here.

def register(request):
    
    form=UserCreationForm()

    return HttpResponseRedirect()
