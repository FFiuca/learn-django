from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'blog.html')

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
