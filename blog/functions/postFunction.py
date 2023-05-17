from blog.models import Post
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from blog.forms import postForm
from django.core.exceptions import ValidationError
from django.core import serializers
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from abc import ABC, abstractmethod
from django.db.models import Q
# import json

@csrf_exempt
def get(request):
    data = Post.objects.all()

    # it mean, only dict or list can return on jsonresponse, so you must convert all values first
    return JsonResponse({
        'status' : 200,
        # 'data' : serializers.serialize(format='json', queryset=data) # return json encode in json
        'data' : list( data.values()) # .values() is python snippet that can convert to list data type from dict
    }, json_dumps_params={'indent': 4})

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


# validation on layer model
@csrf_exempt
def add2(request):
    add = None

    try:
        add = Post(request.POST or None)

        # samethink with below, just directly call clean_fields, clean, validate_unique in one method
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
        add.save()

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


@csrf_exempt
@api_view(['POST']) # this decorators will perform check is authenticated or not also
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# @permission_required(['blog.add_post', 'blog.delete_post10'], raise_exception=True) # now, the user must have all of the permissions listed
@permission_required(['blog.add_post'] or [ 'blog.delete_post'], raise_exception=True) # now any of the permissions listed match user, will be execute, use Or logic, any other way is make decorator by our self. look random.txt
def add3(request):
    add = None

    # print('\'')
    print(request.user)
    # print('\'')
    try:
        add = postForm.PostModelForm(request.POST)

        if add.is_valid():
            #  this directly save from form model validation
            add.save()
            # print(add)
        else :
            raise ValidationError(add.errors)
    except ValidationError as e:
        return JsonResponse({
            'status' : 500,
            'data' : {
                'error' : str(e)
            }
        }, json_dumps_params={'indent': 4})

    return JsonResponse({
        'status' : 200,
        'data' : ''
    }, json_dumps_params={'indent':4})


@csrf_exempt
def get1(request):
    param = ()

    pk = request.POST.get('pk') or None
    if pk is not None :
        # Q is useful to make dynamic query, just join and assemble at the end
        param= param + (Q(pk=pk),)

    print(param)
    # assembling param tuple using * 
    param = Q(*param)
    data = Post.objects.filter(param).all()

    return JsonResponse({
        'status' : 200,
        # 'data' : serializers.serialize(format='json', queryset=data) # return json encode in json
        'data' : list( data.values()) # .values() is python snippet that can convert to list data type from dict
    }, json_dumps_params={'indent': 4})
