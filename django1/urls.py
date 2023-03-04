"""django1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import sys
import pathlib

from django.contrib import admin
from django.urls import path, re_path, include

# from ..views import first

from .views import first
from blog import views as blogViews
from about import views as aboutViews

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^index$', first.index),
    re_path(r'^index2$', first.index2),
    re_path(r'^about$', aboutViews.index),

    # traditional
    # re_path(r'^blog$', blogViews.index),

    # using app include, will jump out to blog app
    path('blog/', include('blog.urls')),
]
