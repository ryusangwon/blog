from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404
from testApp.models import User
from .forms import UserForm

# Create your views here.

def index(request):
    #return HttpResponse('<h2> Hello, World! </h2>')
    context = dict()
    today = datetime.today().date()
    users = User.objects.all()
    context = {'date':today}
    context['users'] = users
    return render(request, 'testApp/index.html', context=context)

def user_detail(request, pk):
    context = dict()
    user = User.objects.get(id=pk)
    context['user'] = user
    return render(request, 'testApp/detail.html', context=context)

def user_create(request):
    if request.method=='POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save()
            return redirect('user-detail', user_id=new_user.id)
    else:
        user_form = UserForm()
    return render(request, 'testApp/form.html', {'form':user_form})