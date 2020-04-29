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
    "term" :["long-term","short-term"],
    "tasks" :{
        "b/w - i/o " : [ ],
        "Api blog" : [],
        "Api calendar" : [],
        "Api docs" : [],
        "resume page" : [],
        "splitor day" : [],
        "live stat" : []
    }

    
}












def index(request):
    context ={"data" : data }
    return render(request,'interface/root.html' , context)

def home(request):
    return render(request,'interface/home.html')

def about(request):
    return render(request,'interface/about.html')    

def me(request):
    return render()        
        