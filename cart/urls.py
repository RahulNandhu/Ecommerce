from django.urls import path
from django.contrib import admin
from . import views

app_name='cart'

urlpatterns = [
    path('/<p>',views.addtocart,name='addtocart'),
    path('cartview', views.cartview, name='cartview'),
    path('remove_cart/<p>', views.remove_cart, name='remove_cart'),
    path('add_cart/<p>', views.add_cart, name='add_cart'),
    path('delete_cart/<p>', views.delete_cart, name='delete_cart'),
    path('order', views.order, name='order'),
    path('order_view', views.order_view, name='order_view'),

]