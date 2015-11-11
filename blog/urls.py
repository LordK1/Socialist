from django.conf.urls import url, include
from blog.views import PostListView, PostDetailView, CategoryDetailView, CategoryListView, PostCreateView, \
    CategoryCreateView

__author__ = 'k1'

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^post/create/$', PostCreateView.as_view(), name='post_create'),
    # url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^categories/$', CategoryListView.as_view(), name='category_list'),
    url(r'^category/(?P<pk>\d+)/$', CategoryDetailView.as_view(), name='category_detail'),
    url(r'^category/create/$', CategoryCreateView.as_view(), name='category_create'),
]
