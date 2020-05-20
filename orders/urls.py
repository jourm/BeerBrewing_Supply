from django.urls import path
from . import views

urlpatterns = [
    path('', views.orders, name='orders'),
    path('register_order', views.register_order, name='register_order'),
    path('ready_to_ship', views.ready_to_ship, name='ready_to_ship')
]
