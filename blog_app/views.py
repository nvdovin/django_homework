from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as g
from blog_app import models

# Create your views here.

class PostsListView(g.ListView):
    model = models.Blog
    template_name = 'blog_app/posts_list.html'


class PostCreateView(g.CreateView):
    model = models.Blog
    template_name = 'blog_app/post_create.html'
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('blog_app:all_posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

