from django.shortcuts import render, redirect
from .forms import NewBlogPost
from .models import Blog
from django.urls import reverse


# Create your views here.


def view_blogs(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)



def add_blog(request):
    if request.method == 'GET':

        form = NewBlogPost
        context = {
            'form': form
        }
        return render(request, 'blog/add_blog.html', context)
    elif request.method == 'POST':
        form = NewBlogPost(request.POST)
        if form.is_valid():
            new_blog = form.save()

    return redirect(reverse(view_blogs))


