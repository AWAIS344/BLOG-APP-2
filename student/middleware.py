
def CustomFunctionMiddleware(get_response):

    def middleware(request):

        print("Before View Called")

        response=get_response(request)

        print("After View Called")


        return response
    
    return middleware