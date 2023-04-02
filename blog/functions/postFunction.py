from blog.models import Post
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from blog.forms import postForm
from django.core.exceptions import ValidationError
# import json

@csrf_exempt
def add(request):
    add = None
    data = postForm.PostForm(request.POST)

    try:
    # print(request.POST.get('title'))
        # print(data.has_error);
        if(data.is_valid()!=True):
            raise ValidationError('Error Validation')

        # add = Post.objects.create(
        #         title= data.cleaned_data.get('title'),  # cleaned_data is data after validation
        #         body= data.cleaned_data.get('body')
        #     )

        # add = Post(
        #     title=request.POST.get('title'),
        #     body=request.POST.get('body'),
        # )
        # add.save()

        # print(add)
    except ValidationError as e:
        return JsonResponse({
            'status' : 400,
            'data' : {
                'error' : data.errors
            }
        }, json_dumps_params={'indent': 4})
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


# validatio on layer model
@csrf_exempt
def add2(request):
    add = None

    try:
        add = Post(request.POST)

        # add.full_clean()

        add.clean_fields()
        add.clean()
        add.validate_unique()

        # add.full

        # add = Post.objects.create(
        #         title= data.cleaned_data.get('title'),  # cleaned_data is data after validation
        #         body= data.cleaned_data.get('body')
        #     )

        # add = Post(
        #     title=request.POST.get('title'),
        #     body=request.POST.get('body'),
        # )
        # add.save()

        # print(add)
    except ValidationError as e:
        return JsonResponse({
            'status' : 400,
            'data' : {
                'error' : e.message_dict
            }
        }, json_dumps_params={'indent': 4})
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
