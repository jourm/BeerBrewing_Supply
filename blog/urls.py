from django.urls import path
from . import views

urlpatterns = [
    path('add_blog', views.edit_blog, name='add_blog'),
    path('', views.view_blogs, name='view_blogs'),
    path(r'^/edit_blog/(?P<blog_id>\d+)$', views.edit_blog, name='edit_blog'),
    path('/edit_blog/', views.edit_blog, name='edit_blog'),
    path('delete_blog/<blog_id>', views.delete_blog, name='delete_blog'),
]

