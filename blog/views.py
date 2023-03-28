from django.shortcuts import render
from django.http import HttpResponse

# models
from .models import Post

# Create your views here.
def index(request):
    context = {
        'post': Post.objects.all()
    }

    print(context)
    return render(request, 'blog.html', context)

def recent(request):
    context = {
        'content' : 'ini content',
        'list' : [
            ['a', 'dadlakdjslk'],
            ['b', 'hasdhkjashd'],
            ['c', {
                'nama' : 'caco',
                'umur' : 25
            }]
        ]
    }

    return render(request, 'recent.html', context)
