# interface/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from django.views.generic import View 
   
#from rest_framework.views import APIView 
#from rest_framework.response import Response 
with open("interface/data.json") as f:
            data=json.load(f)
            f.close 
 
def dump_data(edited_data):
        with open("interface/data.json","w") as f:
            json.dump(edited_data,f)
            f.close

def index0(request):
    context ={"data" : data }
    if request.method=="POST":
        hackthone_name=request.POST['hackthone_name']
        hackthone_start=request.POST['hackthone_start']
        hackthone_end=request.POST['hackthone_end']
        hackthone_link=request.POST['hackthone_link']
        hackthone_reg=request.POST['hackthone_reg']    
        data["hackthones"][hackthone_name]=[ hackthone_start, hackthone_end, hackthone_link, hackthone_reg]
        dump_data(data)
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