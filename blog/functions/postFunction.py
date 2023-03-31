from blog.models import Post
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# import json

@csrf_exempt
def add(request):
    add = None
    try:
    # print(request.POST.get('title'))
    # add = Post.objects.create( title =  request.POST.get('title'), body = request.POST.get('body'), )

        add = Post(
            title=request.POST.get('title'),
            body=request.POST.get('body'),
        )
        add.save()

        print(add)
    except Exception as e:
        return JsonResponse({
            'status' : 500,
            'data' : {
                'error' : str(e)
            }
        }, json_dumps_params={'indent': 4}) # indent use to number of indent/space tab when print json prettier

    return JsonResponse({
        'status' : 200,
        'data' : ''
    }, json_dumps_params={'indent': 4})