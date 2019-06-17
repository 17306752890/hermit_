# _*_ coding: utf-8 _*_

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^register/$', views.UserRegister.as_view()),
    # url(r'^login/$', UserLogin.as_view()),
    url(r'^login/$', views.login),
]
