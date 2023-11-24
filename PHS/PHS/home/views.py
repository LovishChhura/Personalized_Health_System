from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return render(request,'user_index.html')

@login_required(login_url="/login/")
def reduce_stress(request):
    return render(request,'reduce_stress.html')

def home(request):
    return render(request,'home.html')

def login_page(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        if not User.objects.filter(email=email).exists():
            messages.error(request,'Invalid email-id')
            return redirect('/login/')
        user=authenticate(email=email,password=password)
        if user is None:
            messages.error(request,'Invalid credentials')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/user/')
            
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user=User.objects.filter(email=email)
        if user.exists():
            messages.info(request,'User already exist')
            return redirect('/register/')
        
        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.save()
        messages.info(request,'Registered Successfully')
        return redirect('/login/')
    return render(request,'login.html')