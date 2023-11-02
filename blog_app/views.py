from typing import Any
from django.db import models
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic as g
from blog_app import models
from my_util_files.transcrypter import transcription

# Create your views here.

class PostsListView(g.ListView):
    model = models.Blog
    template_name = 'blog_app/posts_list.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_published=True).order_by('views_counter').reverse()
        return queryset


class PostCreateView(g.CreateView):
    model = models.Blog
    template_name = 'blog_app/post_create.html'
    fields = ('title', 'content', 'preview')
    success_url = reverse_lazy('blog_app:all_posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post = transcription(new_post.title)
            print(new_post)
            new_post.save()
        return super().form_valid(form)
    

class PostUpdateView(g.UpdateView):
    model = models.Blog
    template_name = "blog_app/post_create.html"
    fields = ('title', 'content', 'preview', 'is_published')
    success_url = reverse_lazy('blog_app:all_posts')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(pk = self.kwargs['pk'])
        return queryset   

    def get_success_url(self) -> str:
        return reverse('blog_app:view', args=[self.kwargs.get('pk')])

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = transcription(new_post.title)
            new_post.save()
        return super().form_valid(form)


class PostDetailView(g.DeleteView):
    model = models.Blog
    template_name = "blog_app/post_view.html"
    context_object_name = 'post_data'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(pk=self.kwargs["pk"])
        return queryset
    
    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object
    
    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post = transcrypter(new_post.title)
            print(new_post)
            new_post.save()
        return super().form_valid(form)
    

class PostDeleteView(g.DeleteView):
    model = models.Blog
    template_name = "blog_app/post_delete.html"
    context_object_name = 'post_data'
    success_url = reverse_lazy('blog_app:all_posts')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(pk=self.kwargs["pk"])
        return queryset
    
