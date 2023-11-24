from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    # path("",views.index,name='index'),
    path("reduce_stress/",views.reduce_stress,name='reduce_stress'),
    path("login/",views.login_page,name='login_page'),
    path("register/",views.register,name='register'),
    path("logout/",views.logout_page,name='logout_page'),
]
