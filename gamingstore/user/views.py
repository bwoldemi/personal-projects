#from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# render index html 
def index(request):
    return render(request,'user/index.html')

# crate sign up form where user register 
def signup(request):
    if request.method=='GET':
        user_form = UserCreationForm()
        return render(request, 'registration/signup.html', {'user_form':user_form})
    elif request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("post clicked ***")
            form.save();
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            return  redirect('/')
        else:
              return render(request, 'registration/signup.html', {'user_form':form})