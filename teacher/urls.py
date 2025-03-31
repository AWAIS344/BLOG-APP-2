from django.urls import path
from .views import Teacher,thanks

urlpatterns = [
    
    path("teacher/",Teacher ,name='teacher' ),
    path("thank-you/",thanks ,name='thanks' )
]
