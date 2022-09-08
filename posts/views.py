from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"