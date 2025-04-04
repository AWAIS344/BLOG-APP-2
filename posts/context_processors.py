

def post(request):

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
    
    
    
    return {"posts":posts}