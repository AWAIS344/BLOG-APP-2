
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

    def __call__(self,request):

        print("Before View Called")

        response=self.get_response(request)

        print("After View Called")


        return response
    
   