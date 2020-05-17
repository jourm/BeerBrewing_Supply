from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('terms', views.terms, name='terms'),
    path('completed', views.completed,
         name='checkout_completed'),
]
