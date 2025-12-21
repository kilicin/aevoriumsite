from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('login', views.login, name='login'),
    path('shop', views.shop),
    path('personal-cabinet', views.personal_cabinet, name= "personal-cabinet"),
    path('start', views.start),
    path('forgot-password', views.forgotPassword),
    path('new-password', views.newPassword),
    path('deposit', views.deposit),
]