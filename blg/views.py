from django.shortcuts import render
from django.views.generic import ListView, DetailView # new
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class DetailView(ListView):
    model = Post
    template_name = 'post_detail.html'
