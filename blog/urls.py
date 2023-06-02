from django.urls import path, re_path
from django.views.decorators.csrf import csrf_exempt

from . import views

from .functions import postFunction

# value = 'huha'

app_name = 'blog' # use for namespace url
urlpatterns = [
    re_path(r'^$', views.index),
    # named url -> called on the view with -> url "name"
    re_path(r'^recent$', views.recent, name='recent'),

    path('post/', postFunction.get),
    path('detail/<int:id>', views.detail, name='detail'),

    path('post/add', postFunction.add, name='post.add'),
    path('post/add2', postFunction.add2, name='post.add2'),
    # path('post/add3', csrf_exempt(postFunction.add3), name='post.add3'),
    path('post/add3', postFunction.add3, name='post.add3'),
    path('post/get1', postFunction.get1, name='post.get1'),
    path('post/getCat', postFunction.getCat, name='post.getCat'),
    path('post/getCat2', postFunction.getCat2, name='post.getCat2'),

    path('post/getPost2', postFunction.getPost2, name='post.getPost2'),
    path('post/getPost3', postFunction.getPost3, name='post.getPost3'),


    # re_path(r'^detail/<int:id>', views.detail),
]
