"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from projectapp.views import random_create_sinks_nodes,index1,index2,people_create_sinks_nodes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1/',index1),
    path('index2/',index2),
    url(r'^create1$',random_create_sinks_nodes),
    url(r'^create2$',people_create_sinks_nodes),
]
