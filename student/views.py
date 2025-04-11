from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

# Create your views here.    


def set(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(home)
    print("view called")

    # x=1/0
    response=TemplateResponse(request,"student/home.html",{})
    response.set_cookie("theme","dark")

    return response




def get(request):

    #use get one if exception i.e what if theme cookies is not available 
    # theme = request.COOKIES.get('theme', 'light_mode')
    
    #else use this without any default value
    
    theme = request.COOKIES['theme']
    response=HttpResponse(f"<h1> Getting the Cookies<h1> <br> {theme}")
  
    return response
    