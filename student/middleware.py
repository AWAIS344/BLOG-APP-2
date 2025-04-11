from django.http import HttpResponse
import logging
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


logger = logging.getLogger(__name__)
class CustomClassMiddleware:

    def __init__(self, get_response):

        self.get_response=get_response
        

        print("one time config")

    def __call__(self, request):
        print("Before View Called")
        
        print(f"Request path: {request.path}")

        if request.path.strip() == '/set/':
            print("Set view is called")

        # Call the view (or the next middleware)
        response = self.get_response(request)

        print("After View Called")

        return response
    
    def process_view(self, request,view_func,view_args,view_kwargs):

        print("Process view ")
        print(view_func.__name__)
        print(view_args)
        return None

    def process_exception(self, request, exception):
        # Log the exception with traceback
        logger.exception("Exception occurred during request processing")

        if isinstance(exception, ZeroDivisionError):
            logger.warning("ZeroDivisionError encountered.")
            return HttpResponse("You can't divide by zero!", status=400)

        if isinstance(exception, KeyError):
            logger.warning("KeyError encountered.")
            return HttpResponse("The Value Missing or has been Deleted!", status=400)

        logger.error("Unhandled exception: %s", str(exception))
        return HttpResponse("Something went wrong", status=500)
    
    def process_template_response(self,request,response):

        response.context_data['developer'] = 'Awais Ali Shah 👨‍💻'
        return response
        
    

    # def __call__(self,request):

    #     print("Before View Called")

    #     print(request.path)

    #     if request.path == '/student/set/':
    #         print("set vire is called")

    #     response=self.get_response(request)

    #     print("After View Called")


    #     return response
    
   