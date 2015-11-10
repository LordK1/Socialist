# Create your views here.
from braces.views import LoginRequiredMixin
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView
from accounts.models import Author

from blog.forms import PostForm
from blog.models import Post, Category


class PostListView(ListView):
    template_name = 'blog/posts.html'
    model = Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'
    model = Post
    context_object_name = 'post'


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'blog/post_create.html'
    model = Post
    # optional
    form_class = PostForm
    login_url = reverse_lazy("login")
    redirect_field_name = "blog:post_list"
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        print(self.request.user)
        post = form.save(commit=False)
        # commit=False tells Django that "Don't send this to database yet.
        # I have more things I want to do with it."
        try:
            author = Author.objects.get(user=self.request.user)
        except Author.DoesNotExist:
            author = Author(user=self.request.user)
            author.save()

        post.author = author
        post.save()
        return HttpResponseRedirect(self.success_url)


class CategoryListView(ListView):
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'
    model = Category


class CategoryDetailView(DetailView):
    template_name = 'blog/category_detail.html'
    context_object_name = 'category'
    model = Category


class CategoryCreateView(CreateView, LoginRequiredMixin):
    template_name = 'blog/category_create.html'
    model = Category
    fields = ['title']
    login_url = settings.LOGIN_REDIRECT_URL
    success_url = reverse_lazy('blog:category_list')
