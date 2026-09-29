from django.urls import path
from blogs.apps import BlogsConfig
from blogs.views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogsConfig.name

urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_list/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_list/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_list/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_list/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
]