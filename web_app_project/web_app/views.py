from django.shortcuts import render, redirect
from .models import Blog
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login


def index(request):
    if request.method == 'POST':
        if request.POST['login']:
            return redirect('logging_in')
    else:
        return render(request, 'index.html', {})


def homepage(request):
    blog = Blog.objects.all()
    return render(request, 'homepage.html', {"blog": blog})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exist!')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email address already being used!')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('logging_in')

        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('register')

    else:
        return render(request, 'register.html')


def logging_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user=user)
            return redirect('homepage')
        else:
            messages.info(request, 'Invalid Username or Password!')
            return redirect('logging_in')
    else:
        return render(request, 'login.html', {})


def logging_out(request):
    logout(request)
    return render(request, 'homepage.html')


def post(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'post.html', {"blog": blog})


def space(request):
    if request.method == 'POST':
        headline = request.POST['headline']
        content = request.POST['content']

        story = Blog.objects.create(headline=headline, content=content)
        story.save()
        return redirect('homepage')

    else:
        return render(request, 'space.html', {})

