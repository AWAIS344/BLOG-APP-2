from django.urls import path
from .views import Teacher_view,thanks

urlpatterns = [
    
    path("teacher/",Teacher_view ,name='teacher' ),
    path("thank-you/",thanks ,name='thanks' )
]
