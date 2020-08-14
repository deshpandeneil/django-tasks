from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Profile


# Create your views here.

def index(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 != password2:
            messages.error(request, 'Passwords don\'t match.')
            return render(request, 'task_2/signUp.html')
        username = request.POST.get('username')
        users = User.objects.filter(username=username)
        if len(users) != 0:
            messages.error(request, 'This username already exists. Try another username.')
            return render(request, 'task_2/signUp.html')
        phone = str(request.POST.get('phone'))
        if len(phone) != 10:
            messages.error(request, 'Please enter valid phone number.')
            return render(request, 'task_2/signUp.html')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        newUser = User.objects.create_user(username=username, email=email, first_name=fname, last_name=lname,
                                           password=password1)
        profile = Profile(user=newUser, phone=phone, gender=gender)
        profile.save()
        newUser.save()
        messages.success(request, 'Your account has been created.')
        return redirect('login')
    return render(request, 'task_2/signUp.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('user-home')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    return render(request, 'task_2/login.html')


def userHome(request):
    return render(request, 'task_2/userHome.html')


def logout(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('sign-up')

def search(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email == '':
            messages.error(request, 'Please enter an email address to search.')
            return redirect('search')
        user = User.objects.filter(email=email)
        if len(user) == 0:
            messages.info(request, 'No user found with the entered email address.')
            return redirect('search')
        else:
            params = {'user': user}
            return render(request, 'task_2/result.html', params)
    return render(request, 'task_2/search.html')
