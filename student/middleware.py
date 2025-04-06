from django.http import HttpResponse
#FUNCTION BASEED MIDDLEWARE

# def CustomFunctionMiddleware(get_response):

#     print("one time config")

#     def middleware(request):

#         print("Before View Called")

#         response=get_response(request)

#         print("After View Called")


#         return response
    
#     return middleware

#CLASS BASED MIDDLEWARE

class CustomClassMiddleware:

    def __init__(self, get_response):

        self.get_response=get_response
        

        print("one time config")

    def __call__(self, request):
        print("Before View Called")
        # print(f"Request path: {request.path}")

        # if request.path.strip() == '/set/':
        #     print("Set view is called")

        # Call the view (or the next middleware)
        response = self.get_response(request)

        print("After View Called")

        return response
    
    # def process_view(self, request,view_func,view_args,view_kwargs):

    #     print("Process view ")
    #     print(view_func.__name__)
    #     print(view_args)
    #     return None

    def process_exception(self,request,exception):

        if isinstance(exception, ZeroDivisionError):
            return HttpResponse("You can't divide by zero!", status=400)
        
        return HttpResponse("Something went wrong.", status=500)
        
    

    # def __call__(self,request):

    #     print("Before View Called")

    #     print(request.path)

    #     if request.path == '/student/set/':
    #         print("set vire is called")

    #     response=self.get_response(request)

    #     print("After View Called")


    #     return response
    
   