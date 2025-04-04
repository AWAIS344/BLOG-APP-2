from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def set(request):

    response=HttpResponse('<h1> Set <h1>')
    response.set_cookie("theme","dark")

    return response