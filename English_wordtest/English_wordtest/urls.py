"""English_wordtest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from English_TESTING import views as word_test_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', word_test_view.start_page, name="index"),
    path('test/<int:step>', word_test_view.word_test, name="test"),
    path('result/', word_test_view.result, name='result'),

]
