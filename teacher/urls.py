from django.urls import path
from .views import Teacher_view,thanks,all_data,update

urlpatterns = [
    
    path("teacher/",Teacher_view ,name='teacher' ),
    path("thank-you/",thanks ,name='thanks' ),

    path("all-data/",all_data ,name='all_data' ),

    path("update/<int:id> " ,update ,name='update' ),

]
