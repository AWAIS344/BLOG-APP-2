from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def set(request):

    
    city = request.session['city']="Mardan"


    return HttpResponse("<h1>Session Addition</h1>")

def get(request):

    city = request.session['city']

    return HttpResponse(f"<h1>Getting Sesssion Contents </h1> <br> {city}")