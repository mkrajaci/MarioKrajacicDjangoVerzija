from django.shortcuts import render
from .models import Post

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'landingPage/home.html', context)


def home_about(request):
    return render(request, 'landingPage/about.html', {'title': 'About'})
