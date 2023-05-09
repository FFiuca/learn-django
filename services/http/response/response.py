from django.http import JsonResponse

class response:
    def __init__(self, statusCode: int,data: dict={}):
        return JsonResponse({
            'status' : statusCode,
            'data' : data
        }, json_dumps_params={'indent':4})

    def response(self, statusCode: int,data: dict={}): 
        return JsonResponse({
            'status' : statusCode,
            'data' : data
        }, json_dumps_params={'indent':4})