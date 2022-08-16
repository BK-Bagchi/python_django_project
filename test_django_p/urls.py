"""test_django_p URL Configuration

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
from django.contrib import admin
from django.urls import path

# this lice needs to be included for url mapping
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # here whatever is created in the "django_app" will be shown to the user
    # writing of this format is used for url mapping
    path('django/', include('django_app.urls'))
]
