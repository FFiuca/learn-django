from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from auth.forms.loginForm import LoginForm
from django.core.exceptions import ValidationError

@csrf_exempt
def login(request):
    data = LoginForm(request.POST)

    try:
        if(data.is_valid()!=True):
            raise ValidationError('Error Validation')

        username = data.cleaned_data.get('username')
        password = data.cleaned_data.get('password')

        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)

            return JsonResponse({
                'status' : 200,
                'data' : {
                    'user' : user
                }
            }, json_dumps_params={'indent' : 4})
        else :
            return JsonResponse({
               'status' : 400,
                'data' : {
                    'user' : user
                }
            }, json_dumps_params={'indent' : 4})
        
    except ValidationError as e:
        return JsonResponse({
            'status' : 500,
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
        }, json_dumps_params={'indent': 4})