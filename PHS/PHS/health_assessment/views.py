from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def index(request):
    return render(request,'health_assessment.html')

@login_required(login_url="/login/")
def bmi(request):
    if request.method=="POST":
        weight=request.POST.get('weight')
        height=request.POST.get('height')
        try:
            weight=float(weight)
            height=float(height)
            if height>0:
                height=height/100
                bmis=weight / (height ** 2)
                bmi_s= str(f'{bmis:.2f}')
                if bmi_s<16:
                    bmiStat="Severe Thinness"
                elif bmis>=16 and bmis<17:
                    bmiStat="Moderate Thinness"
                elif bmis>=17 and bmis<18.5:
                    bmiStat="Mild Thinness"
                elif bmis>=18.5 and bmis<25:
                    bmiStat="Normal"
                elif bmis>=25 and bmis<30:
                    bmiStat="Overweight"
                elif bmis>=30 and bmis<35:
                    bmiStat="Obese Class 1"
                elif bmis>=35 and bmis<40:
                    bmiStat="Obese Class 2"
                elif bmis>=40:
                    bmiStat="Obese Class 3"
                else:
                    bmiStat=""
                return render(request,"health_assessment.html",{'score':bmi_s,'statusB':bmiStat})
            else:
                er="Enter numeric number than Zero"
                return render(request,'health_assessment.html',{'cat':'cat1','message':er})
        except:
            er="Enter numeric number"
            return render(request,'health_assessment.html',{'cat':'cat1','message':er})
    return render(request,'health_assessment.html')

@login_required(login_url="/login/")
def gr1(request):
    if request.method=="POST":
        level=request.POST.get('mgdlGR')
        try:
            level=float(level)
            if level<140:
                bs='normal'
            elif level>=140 and level >199:
                bs='prediabetic'
            elif level >200:
                bs="diabetic"           
            else:
                bs=""
            return render(request,"health_assessment.html",{'status1':bs})
        except:
            er="Enter numeric number"
            return render(request,'health_assessment.html',{'cat':'cat2','message':er})       
    return render(request,'health_assessment.html')

