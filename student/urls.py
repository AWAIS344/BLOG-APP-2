from django.urls import path
from .views import set,get

urlpatterns = [
    path("set/" ,set ),
    path("get/" ,get )
    
]
