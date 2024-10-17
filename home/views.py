from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from home.models import Info

#from django.contrib.auth.hashers import make_password  # Import password hashing function

def signupuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('Confirm_password')


        if password == confirm_password:
            info=Info(username=username,phone=phone,password=password)
            info.save()
            user=User.objects.create_user(username=username,password=password)
            user.save()
            messages.success(request, "Passwords do not match!")
            return redirect("/login")
        else:
            messages.error(request, "Passwords do not match!")
            return redirect("/signup")
    else:
        return render(request, 'signup.html')

def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'index.html')

def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    

    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")




