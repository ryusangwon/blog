from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404

# Create your views here.

def index(request):
    #return HttpResponse('<h2> Hello, World! </h2>')
    today = datetime.today().date()
    context = {'date':today}
    return render(request, 'testApp/index.html', context=context)

def word_detail(request, word):
    if word == 'error':
        raise Http404('RAISE ERROR')
    context = {'name':word}
    context['img_path'] = 'testApp/images/banana.jpg'
    return render(request, 'testApp/detail.html', context=context)