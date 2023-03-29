from django.urls import path, re_path

from . import views

# value = 'huha'

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^recent$', views.recent),

    path('detail/<int:id>', views.detail),
    # re_path(r'^detail/<int:id>', views.detail),
]
