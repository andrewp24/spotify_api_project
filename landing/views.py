from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'blog post 1',
        'content': 'first post',
        'date_posted': 'august 27, 2018'
    },
    {
        'author': 'jane doe',
        'title': 'blog post 2',
        'content': '2nd post',
        'date_posted': 'august 27, 2018'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'landing/home.html', context)


def about(request):
    return render(request, 'landing/about.html', {'title': 'about'})
