from django.urls import path, re_path, include
from rest_framework_simplejwt import views as jwtViews

app_name = 'api'

urlpatterns = [
    path('token', jwtViews.TokenObtainPairView.as_view(), name='tokenObtainPair'),
    path('token/refresh', jwtViews.TokenRefreshView.as_view(), name='tokenRefresh')
]

