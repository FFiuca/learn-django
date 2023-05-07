from django.urls import path, re_path

from auth.functions import AuthFunct

app_name = 'auth'
urlpatterns = [
    re_path('login', AuthFunct.auth_login),

]
