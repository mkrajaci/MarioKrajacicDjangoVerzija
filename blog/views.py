from django.shortcuts import render
from landingPage.models import Post

# Create your views here.


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def blog_about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


