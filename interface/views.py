# interface/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse


data ={
    "user" : "infinity8sailor" ,
    "icon" : "interface/images/me.jpg",
    "projects" : {
        "glass-Ai" :[],
        "#SE" : [],
        "RoboCup@Home" : []
    },
    "terms" :["long-term","short-term"],
    "tasks" :{
        "b/w - i/o " : [ 80],
        "Api blog" : [50],
        "Api calendar" : [50],
        "Api docs" : [70],
        "resume page" : [40],
        "splitor day" : [60],
        "live stat" : [20],
        "connectivity": [10],
        "project_session": [40],
        "passion": [20]
    }

    
}












def index(request):
    context ={"data" : data }
    return render(request,'interface/root.html' , context)

def home(request):
    return render(request,'interface/home.html')

def about(request):
    return render(request,'interface/index.html')    

def docs(request):
    return render(request, 'interface/docs.html')        
        