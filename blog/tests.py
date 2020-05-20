from django.test import TestCase
from .models import Blog

# Create your tests here.

class TestBlog(TestCase):
    def test_view_blogs(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')


    def test_add_blog(self):
        response = self.client.get('/blog/add_blog')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_blog.html')


    def test_add_blog_post(self):
        response = self.client.post('/blog/add_blog')
        self.assertEqual(response.status_code, 302)


    def test_edit_blog(self):
        blog = Blog.objects.create(
            title='hej',
            author='hopp',
            content='hej'
        )
        blog.save()
        response = self.client.get('/blog/edit_blog/' + str(blog.id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/edit_blog.html')

    def test_edit_blog_post(self):
        blog = Blog.objects.create(
            title='hej',
            author='hopp',
            content='hej'
        )
        blog.save()
        response = self.client.post('/blog/edit_blog/' + str(blog.id),{
            'title': 'hej',
            'author': 'hopp',
            'content': 'hejsan'
        })
        self.assertEqual(response.status_code, 302)


