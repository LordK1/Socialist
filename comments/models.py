from django.db import models

# Create your models here.
from django_comments.models import Comment


class PostComment(Comment):
    content = models.CharField(max_length=300)

    class Meta:
        app_label = "comments"
        verbose_name_plural = "Comments"
        verbose_name = "Comment"
