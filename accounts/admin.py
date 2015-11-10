from django.contrib import admin


# Register your models here.
from accounts.models import Author
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'created_date', 'published_date', 'author', 'category'
    )
    list_filter = ('created_date', 'published_date')
    search_fields = ('title',)
    list_display_links = ('author', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')
    list_filter = ('created_date',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'genres', 'created_date')
    list_filter = ('genres', 'created_date')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
