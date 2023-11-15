from django.shortcuts import render,redirect
import pandas as pd

df=pd.read_excel("./datasets/PHS_exercise_data.xlsx")
# Create your views here.
def index(request):
    return redirect('/#yoga')

def yoga_view(request, yoga_name):
    return render(request,'yoga.html')