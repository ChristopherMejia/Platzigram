from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#exceptions
from django.db.utils import IntegrityError  

#Models
from django.contrib.auth.models import User
from users.models import Profile

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

def signup (request):
    """sign up"""
    if request.method =='POST':
        username = request.POST['username']
        passwd = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        if passwd != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})
        
        try:
            user = User.objects.create_user(username = username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})


        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()


    return render(request, 'users/signup.html')


def update_profile(request):
    """Update a user's profile view"""
    profile = request.user.profile
    return render(
        request = request,
        template_name ='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user
        }
    )
