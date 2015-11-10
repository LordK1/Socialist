from django.core.urlresolvers import reverse, reverse_lazy
from django.db import models

from accounts.models import Author


class Category(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ('-created_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'pk': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='posts')
    author = models.ForeignKey(Author, related_name='posts')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-created_date',)

    def __str__(self):
        return "%s" % self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.pk})
