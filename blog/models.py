from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=300, unique=True)
    author = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    uppdated = models.DateTimeField(auto_now= True)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
