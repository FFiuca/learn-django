from django.urls import path, re_path
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
    path('post/add3', postFunction.add3, name='post.add3'),

    # re_path(r'^detail/<int:id>', views.detail),
]
