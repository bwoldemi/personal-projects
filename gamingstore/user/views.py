#from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render



# Create your views here.
def index(request):
    return render(request,'user/index.html')
def register(request):
    return render(request, 'user/register.html')
