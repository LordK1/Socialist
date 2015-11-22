from django.contrib import admin

# Register your models here.
from comments.models import PostComment

admin.site.register(PostComment)
