from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'user_index.html')

def reduce_stress(request):
    return render(request,'reduce_stress.html')

def home(request):
    return render(request,'home.html')

def login_page(request):
    return render(request,'login.html')