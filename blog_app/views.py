from typing import Any
from django.db import models
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic as g

from blog_app import models
from blog_app import forms as f

from my_util_files.transcrypter import transcription

from django.contrib.auth import mixins
from django.contrib.auth import decorators as d

# Create your views here.

class PostsListView(g.ListView):
    model = models.Blog
    template_name = 'blog_app/posts_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            if user.is_staff or user.is_superuser or user.has_perm('blog_app.change_blog'):
                pass
            else:
                queryset = queryset.filter(is_published=True).order_by('views_counter').reverse() | queryset.filter(author=user).order_by('views_counter').reverse()
        else:
            queryset = queryset.filter(is_published=True).order_by('views_counter').reverse()
        return queryset


class PostCreateView(mixins.LoginRequiredMixin, g.CreateView):
    model = models.Blog
    template_name = 'blog_app/post_create.html'
    form_class = f.BlogCreateForm
    success_url = reverse_lazy('blog_app:all_posts')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["editing"] = False
        return context

    def form_valid(self, form):
        if form.is_valid():
            new_post = form.save()
            new_post.slug = transcription(new_post.title)
            new_post.save()

            w = form.save(commit=False)
            w.author = self.request.user
        return super().form_valid(form)
    

class PostUpdateView(mixins.LoginRequiredMixin, g.UpdateView):
    model = models.Blog
    template_name = "blog_app/post_create.html"
    form_class = f.BlogCreateForm
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
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["editing"] = True
        return context


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
            new_post = transcription(new_post.title)
            print(new_post)
            new_post.save()
        return super().form_valid(form)


class PostDeleteView(mixins.LoginRequiredMixin, g.DeleteView):
    model = models.Blog
    template_name = "blog_app/post_delete.html"
    context_object_name = 'post_data'
    success_url = reverse_lazy('blog_app:all_posts')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset.filter(pk=self.kwargs["pk"])
        return queryset


@d.permission_required('blog_app.change_blog')
def change_publish_status(requesr, pk):
    blog = get_object_or_404(models.Blog, pk=pk)    
    if blog.is_published == True:
        blog.is_published = False
    else:
        blog.is_published = True
    blog.save()
    return redirect(reverse('blog_app:all_posts'))

