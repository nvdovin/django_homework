from django.shortcuts import render
from django.views import generic as g
from blog_app import models

# Create your views here.

class PostsListView(g.ListView):
    model = models.Blog
    template_name = 'blog_app/posts_list.html'
    
