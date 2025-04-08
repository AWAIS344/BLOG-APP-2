from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def set(request):
    request.session['name']={"name1":"Awais","name2":"Sudais"}
    request.session['city']="Mardan"


    return HttpResponse("<h1>Session Addition</h1>")

def get(request):
    name=request.session["name"]
    city = request.session['city']

    return HttpResponse(f"<h1>Getting Sesssion Contents </h1> <br> {name}")

def delete(request):

    request.session.flush()   #use if you want to also delete session from datase
    del request.session['city']  #use if you wanna just delete from session(browser) just
    return HttpResponse("<h1>deleted</h1>")

def update(request):

    request.session['name']['name1'] = "Sudais"

    request.session.modified = True
    return HttpResponse("<h1>Getting Updated </h1>")
