from django.shortcuts import render,redirect
import pandas as pd

df=pd.read_excel("./datasets/PHS_exercise_data.xlsx")
# Create your views here.
def index(request):
    return redirect('/#exercise')

def exercise_view(request, exercise_name):
    # Now, exercise_name contains the part of the URL after '/exercise/'
    # You can use it as needed
    # Filter the DataFrame to get rows where the specified column matches the target category
    filtered_df = df[(df[exercise_name] == 1) & (df['Beginner'] == 1)]
    # Specify the number of random rows you want to select
    num_random_rows = 4  # Adjust this number as needed
    # Get random rows from the filtered DataFrame
    random_rows = filtered_df.sample(n=num_random_rows)
    filtered_df2 = df[(df[exercise_name] == 1) & (df['Advanced'] == 1)]
    random_rows2 = filtered_df2.sample(n=num_random_rows)
    namelist=[]
    linklist=[]
    namelist.extend(random_rows.Exercise.to_list())
    namelist.extend(random_rows2.Exercise.to_list())
    linklist.extend(random_rows.Links.to_list())
    linklist.extend(random_rows2.Links.to_list())
    params={'name':exercise_name.capitalize(),'b1i':namelist[0].lower(),'b2i':namelist[1].lower(),'b3i':namelist[2].lower(),'b4i':namelist[3].lower(),'b1':namelist[0],'b2':namelist[1],'b3':namelist[2],'b4':namelist[3],'b1L':linklist[0],'b2L':linklist[1],'b3L':linklist[2],'b4L':linklist[3],'a1i':'/static/media/gym exercises/'+namelist[4].lower()+'.jpg','a2i':namelist[5].lower(),'a3i':namelist[6].lower(),'a4i':namelist[7].lower(),'a1':namelist[4],'a2':namelist[5],'a3':namelist[6],'a4':namelist[7],'a1L':linklist[4],'a2L':linklist[5],'a3L':linklist[6],'a4L':linklist[7]}
    return render(request,'exercises.html',params)