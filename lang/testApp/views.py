from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from testApp.models import User

# Create your views here.

def index(request):
    #return HttpResponse('<h2> Hello, World! </h2>')
    context = dict()
    today = datetime.today().date()
    users = User.objects.all()
    context = {'date':today}
    context['users'] = users
    return render(request, 'testApp/index.html', context=context)

def word_detail(request, pk):
    context = dict()
    user = User.objects.get(id=pk)
    context['user'] = user
    return render(request, 'testApp/detail.html', context=context)