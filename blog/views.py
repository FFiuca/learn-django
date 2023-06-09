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
    Post.objects.filter(id=1).get()

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

def detail(request, id):
    # print(request)
    # return HttpResponse('aa')
    context = {
        'data' : Post.objects.get(pk=id)
    }

    return render(request, 'detail.html', context)



