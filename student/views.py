from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def set(request):


    print("view called")

    # x=1/0
    response=HttpResponse('<h1> Set <h1>')
    response.set_cookie("theme","dark")

    return response


def get(request):

    #use get one if exception i.e what if theme cookies is not available 
    # theme = request.COOKIES.get('theme', 'light_mode')
    
    #else use this without any default value
    
    theme = request.COOKIES['theme']
    response=HttpResponse(f"<h1> Getting the Cookies<h1> <br> {theme}")
  
    return response
    