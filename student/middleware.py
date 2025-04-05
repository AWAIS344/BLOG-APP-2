
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
        print(f"Request path: {request.path}")

        if request.path.strip() == '/set/':
            print("Set view is called")

        # Call the view (or the next middleware)
        response = self.get_response(request)

        print("After View Called")

        return response

    # def __call__(self,request):

    #     print("Before View Called")

    #     print(request.path)

    #     if request.path == '/student/set/':
    #         print("set vire is called")

    #     response=self.get_response(request)

    #     print("After View Called")


    #     return response
    
   