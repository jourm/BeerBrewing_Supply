from django.urls import path
from . import views

urlpatterns = [
    path('add_blog', views.add_blog, name='add_blog'),
    path('', views.view_blogs, name='view_blogs'),
]
