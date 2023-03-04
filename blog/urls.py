from django.urls import path, re_path

from . import views

# value = 'huha'

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^recent$', views.recent),
]
