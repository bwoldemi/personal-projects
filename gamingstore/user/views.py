#from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

from django import forms

# Create your views here.
def index(request):
    return render(request,'user/index.html')
def register(request):
    if request.method=='GET':
        print("** a get request ")
        return render(request, 'user/register.html')
    elif request.method=='POST':
        class ExampleForms(forms.Form):
            firstname=forms.CharField()
        return render(request,'user/register.html')
