from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
GENRES = (
    (1, 'Not Relevant'),
    (2, 'Male'),
    (3, 'Female'),
)


class Author(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    genres = models.IntegerField(choices=GENRES, default=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.email

    def get_absolute_url(self):
        return reverse('author', kwargs={'pk': self.pk})
