from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
    """Login view"""
    #import pdb; pdb.set_trace()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed') 
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})


    return render(request, 'users/login.html')

def logout_view(request):

    logout(request)
    return redirect('login')
