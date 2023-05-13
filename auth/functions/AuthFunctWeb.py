from django.contrib.auth import authenticate, login, logout, decorators
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from auth.forms.loginForm import LoginForm
from django.forms.models import model_to_dict
from django.shortcuts import redirect, resolve_url
from services.http.response.response import response

def auth_login(request):
    data = None

    try:
        data = LoginForm(request.POST)
    except Exception as e :
        return redirect(to='login', kwargs={
            'email' : request.POST.get('email')
        })

    return redirect(to='dashboard')