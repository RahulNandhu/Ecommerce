from django.contrib import admin
from django.urls import path
from . import views
app_name='shop'

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<p>', views.products, name='products'),
    path('details/<p>', views.details, name='details'),
    path('register', views.u_register, name='register'),
    path('login', views.u_login, name='login'),
    path('logout', views.u_logout, name='logout'),

]