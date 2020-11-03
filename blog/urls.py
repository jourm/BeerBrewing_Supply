from django.urls import path
from . import views

urlpatterns = [
    path('add_blog', views.blog_edit, name='add_blog'),
    path('', views.view_blogs, name='view_blogs'),
    path('edit_blog/<blog_id>', views.blog_edit, name='edit_blog'),
    path('delete_blog/<blog_id>', views.delete_blog, name='delete_blog'),
]
