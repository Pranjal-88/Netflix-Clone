from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from .models import Movie

def logout(request):
    auth.logout(request)
    return redirect("login")

def movie(request,movie_name):
    movie_obj=Movie.objects.get(movie_name=movie_name)
    return render (request,"movie.html",{"movie":movie_obj})

def index(request):
    movies=Movie.objects.all()
    return render(request,"index.html",{'movies':movies})

def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        pwd=request.POST["password"]
        new_user=auth.authenticate(username=username,password=pwd)
        if new_user is None:
            messages.info(request,"Invalid Credentials")
            return redirect("login")
        else:
            auth.login(request,new_user)
            return redirect("/")
    return render(request,"login.html")

def signup(request):
    if request.method=="POST":
        email=request.POST["email"]
        username=request.POST["username"]
        pwd1=request.POST["password"]
        pwd2=request.POST["password2"]
        if pwd1==pwd2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already registered")
                return redirect("signup")
            else:
                new_user=User.objects.create_user(username=username,email=email,password=pwd1)
                new_user.save()
                return redirect("/")
        else:
            messages.info(request,"Password don't match")
            return redirect("signup")


    return render(request,"signup.html")
