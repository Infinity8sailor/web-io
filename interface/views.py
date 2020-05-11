# interface/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views.generic import View 
   
#from rest_framework.views import APIView 
#from rest_framework.response import Response 


data1 ={
    "user" : "infinity8sailor" ,
    "icon" : "interface/images/me.jpg",
    "projects" : [
        ["glass-Ai",10,40],
        ["#SE" ,20,70],
        ["RoboCup@Home", 85, 40],
        ["interface" , 100, 50],
        ["wave-io", 10, 70],
        ["mL + Ai" , 20, 60],
        ["vit-Edi", 70, 50]
    ],
    "terms" :["long-term","short-term"],
    "tasks" :[
        ["b/w - i/o " , 80],
        ["Api blog" , 50],
        ["Api calendar" ,50],
        ["Api docs" ,70],
        ["resume page" ,40],
        ["splitor day" ,60],
        ["live stat" , 20],
        ["connectivity", 10],
        ["project_session", 40],
        ["passion", 20]
    ],
    "hackthones" : [
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],
        ["mechathone","20 may", "5 june" , "Done"],

        
    ]

    
}



def index0(request):
    context ={"data" : data1 }
    return render(request,'interface/root.html' , context)

def index(request):
    context ={"data" : data1 }
    return render(request,'interface/root.html' , context)    

def home(request):
    return render(request,'interface/home.html')

def charts(request):
    return render(request,'interface/charts.html')    

def docs(request):
    return render(request, 'interface/docs.html')        

"""
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
        chartdata = [10,30,20,10,10,60,40,20,30,100,20,70,10,10,10,20,30,0,] 
        chartdata1= [100,30,80,40,80,40,40,30,10,20,60,50,50,0,70,40,80,50,]
        data ={ 
                     "labels":labels, 
                     "chartLabel":chartLabel, 
                     "chartdata":chartdata,
                     "chartdata1" : chartdata1, 
             } 
        return Response(data)    
        

        """