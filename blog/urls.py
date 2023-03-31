from django.urls import path, re_path
from . import views

# value = 'huha'

app_name = 'blog' # use for namespace url
urlpatterns = [
    re_path(r'^$', views.index),
    # named url -> called on the view with -> url "name"
    re_path(r'^recent$', views.recent, name='recent'),

    path('detail/<int:id>', views.detail, name='detail'),
    # re_path(r'^detail/<int:id>', views.detail),
]
