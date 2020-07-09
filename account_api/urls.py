from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_account/', views.create_account),
    path('login/', views.login_user),
    path('test/', views.send_email),
]