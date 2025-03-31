from django.shortcuts import render
from django.http import Http404 , HttpResponse
from django.shortcuts import get_object_or_404

from .models import Posts

# Create your views here.

posts=[
    {
        "id":0,"name":"Django","content":"Django is very powerful Python Based framework"
    },
    {
        "id":1,"name":"React","content":"React is very powerful Js Based framework"
    },
    {
        "id":2,"name":"Node Js","content":"Node Js is very powerful Js framework widely used"
    },
]





def Home(request):
    posts=Posts.objects.all()
    context={"posts":posts}
    return render(request , "index.html",context)



def PostPage(request,id):

    sel_post = next((post for post in posts if post["id"] == id), None)

    if sel_post is None:  # If no match found, raise 404
        raise Http404()
        
    context={"post":sel_post}
    return render(request,"post.html",context)