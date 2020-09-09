from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render,redirect
from datetime import datetime
from . models import *
import sklearn
from django.contrib.auth.models import User
from pickle import load
import json
import urllib.request

def Home(request):
  error = False
  error2 = False
  msg = False
  alldis = districs.objects.all()

  allstates = states.objects.all()
  if request.method == "POST":
         d = request.POST
         n = d['name']
         e = d['email']
         m = d['Mobail']
         a = d['aadhar']
         p = d['password']
         cp = d['confirmpassword']
         id = d['id']
         size = d['size']
         lan = d['cars']
         g = d['gender']
         dis = d['districs']
         st = d['states']
         disdata = districs.objects.get(id = dis)
         statesdata = states.objects.get(id = st)
         i = request.FILES['photo']
         data = User.objects.filter(username = m)
         if data:
             error = True
         elif cp!=p:
             error2 = True
         else:
                 msg = True
                 u = User.objects.create_user(username = m,password=p)
                 User_detail.objects.create(usr = u,name = n, email = e,mobile = m,aadhar = a,id_proof = id,photo = i,language = lan,  gender =   g,
                 size = size, dis = disdata, states1 = statesdata)
  model = load(open("C:\\Users\\HP\\Desktop\\raghav\\mysite\\SIH\\Pickle_RL_Model.pkl", "rb"))

  sale = model.predict([[-1.20866,-0.499955,-0.240362,0.301105]])


  dd = {"error":error,"error2":error2,"msg":msg,"alldis":alldis,"allstates": allstates,"a":sale}
  return render(request,'page.html',dd)

def Login(request):
    error = False
    if request.method == "POST":
         d = request.POST
         m = d['mob']
         p = d['password']
         user = authenticate(username = m,password = p)
         if user:
             login(request,user)

             return redirect('se')
         else:
             error = True
    dd = {"error": error}
    return render(request,'page.html',dd)





def Logout(request):
    logout(request)
    return redirect('l')




def SEcond(request):
   us = request.user
   udata = User_detail.objects.filter(usr = us).first()
   notes = districs_notes.objects.filter(dis = udata.dis)
   notes1 = states_notes.objects.filter(states1 = udata.states1)
   d = {"notes":notes,"notes1":notes1}
   return render(request,'home.html',d)


def about(request):
   return render(request,'about.html')

def Gov(request):
   return render(request,'gov.html')

def Loan(request):
   return render(request,'Loan.html')

def scheme(request):
   return render(request,'scheme.html')

def graph(request):
   return render(request,'graph.html')

def Add():
    s = "Andhra_Pradesh Arunachal_Pradesh Assam Bihar Chhattisgarh Goa Gujarat Haryana Himachal_Pradesh Jharkhand Karnataka Kerala Madhya_Pradesh Maharashtra Manipur Meghalaya Mizoram Nagaland Odisha Punjab Rajasthan Sikkim Tamil_Nadu Telangana Tripura Uttar_Pradesh Uttarakhand West_Bengal"
    li = s.split()
    for i in li:
        states.objects.create(name = i)

def ml():
    model = load("C:\\Users\\HP\\Desktop\\raghav\\mysite\\SIH\\Pickle_RL_Model.pkl")
    model.predict()



def index(request):
    us = request.user
       udata = User_detail.objects.filter(usr = us).first()
       city = districs.objects.filter(dis = udata.dis)
    if request.method == 'POST':
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=indore&appid=5015184dd36bd3631658ee1d30f3ec0e').read()
        list_of_data = json.loads(source)
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            }
    else:
        data ={}
    return render(request, "page.html", data)