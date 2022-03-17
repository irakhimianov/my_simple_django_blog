from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'blog_site/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_site/post.html'


class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_site/post_new.html'
    fields = ['title', 'author', 'body']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog_site/post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_site/post_delete.html'
    success_url = reverse_lazy('home')
