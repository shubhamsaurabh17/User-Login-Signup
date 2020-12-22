"""UserLoginSignup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from TestApp import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^token/', obtain_jwt_token),
    url(r'^$', views.home),
    url(r'^exam/', views.exam),
    url(r'^signup/', views.signup_view),
    url(r'^logout/', views.logout_view),
    url(r'^api/', views.api),
    url(r'^createapi/', views.CreateUserAPI.as_view()),
    url(r'^retrieveapi/(?P<id>\d+)/$', views.RetrieveUserAPI.as_view()),
]
