import os

import django.conf
from django.conf import settings

from blogs.models import BlogPost
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import BlogPostForm


# Create your views here.

class BlogListView(ListView):
    model = BlogPost
    paginate_by = 3

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('blogs:blog_list')
    permission_required = 'blogs.add_blogpost'
    raise_exception = True


class BlogDetailView(DetailView):
    model = BlogPost
    success_url = reverse_lazy('blogs:blog_list')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()

        if self.object.views_count == 100:
            from_email = settings.EMAIL_HOST_USER
            to_email = [os.getenv("EMAIL_TO")]

            send_mail(
                "Ваш Блог",
                "Поздравляем! Вау, ваш пост набрал 100 просмотров.",
                from_email,
                to_email,
                fail_silently=False,
            )

        return self.object


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('blogs:blog_list')
    permission_required = 'blogs.change_blogpost'
    raise_exception = True

    def get_success_url(self):
        return reverse('blogs:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = BlogPost
    success_url = reverse_lazy('blogs:blog_list')
    permission_required = 'blogs.delete_blogpost'
    raise_exception = True
