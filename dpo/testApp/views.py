from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return render(request, 'testApp/index.html')
    return HttpResponse('<h2> test <h2>')