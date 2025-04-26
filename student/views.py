from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from django.template.response import TemplateResponse

# Create your views here.    


def set(request):
    login=reverse("login")
    if not request.user.is_authenticated:
        return HttpResponseRedirect(login)
    else:

        if request.method == 'POST':
            logout(request)
            HttpResponseRedirect(login)
        # x=1/0
        response=TemplateResponse(request,"student/home.html",{})
        response.set_cookie("theme","dark")

        return response




def get(request):

    
    
    theme = request.COOKIES['theme']
    response=HttpResponse(f"<h1> Getting the Cookies<h1> <br> {theme}")
  
    return response
    