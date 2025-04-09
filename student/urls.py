from django.urls import path
from .views import set,get

urlpatterns = [
    path("set/" ,set, name="home"),
    path("get/" ,get )
    
]
