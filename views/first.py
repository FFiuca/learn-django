from django.http import HttpResponse

# method index
def index(request):
    return HttpResponse('Hello World!')
