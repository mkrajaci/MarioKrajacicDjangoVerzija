from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Mario',
        'title': 'Title 1',
        'content': 'Prvi content',
        'date_posted': 'Svibanj 14, 2019',
    },
    {
        'author': 'Marija',
        'title': 'Title 2',
        'content': 'Drugi content',
        'date_posted': 'Svibanj 15, 2019',
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'landingPage/home.html', context)


def home_about(request):
    return render(request, 'landingPage/about.html', {'title': 'About'})
