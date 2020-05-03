# interface/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import View 
   
from rest_framework.views import APIView 
from rest_framework.response import Response 


data1 ={
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
    context ={"data" : data1 }
    return render(request,'interface/root.html' , context)

def home(request):
    return render(request,'interface/home.html')

def about(request):
    return render(request,'interface/index.html')    

def docs(request):
    return render(request, 'interface/docs.html')        

class HomeView(View): 

    def get(self, request, *args, **kwargs): 
        context ={"data" : data1 }
        return render(request, 'interface/root.html' , context) 
   

  
class ChartData(APIView): 
    authentication_classes = [] 
    permission_classes = [] 
   
    def get(self, request, format = None): 
        labels = [ 
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10',
            '11',
            '12',
            '13',
            '14',
            '15',
            '16',
            '17',
            '18',
        ]
        chartLabel = "my data"
        chartdata = [10,30,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,] 
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata, 
             } 
        return Response(data)    
        