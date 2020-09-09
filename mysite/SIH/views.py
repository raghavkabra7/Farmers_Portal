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
import pickle
from pickle import dump
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import numpy as np
import pandas as pd
import urllib # Python URL functions
import urllib.request as urllib2 # Python URL functions



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
                 User_detail.objects.create(usr = u,name = n, email = e,mobile = m,aadhar = a,id_proof = id,photo = i,language = lan,gender = g,
                 size = size, dis = disdata, states1 = statesdata)





  dd = {"error":error,"error2":error2,"msg":msg,"alldis":alldis,"allstates": allstates}
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
    return redirect('home')

def SEcond(request):
   us = request.user
   udata = User_detail.objects.filter(usr = us).first()
   notes = districs_notes.objects.filter(dis = udata.dis)
   notes1 = states_notes.objects.filter(states1 = udata.states1)
   districs = User_detail.objects.filter()
   userdata = User_detail.objects.filter(usr = request.user).first()

   area=int(userdata.size)
   temp=int(17)
   district=userdata.dis.name
   district=district.upper()
   ypred = {}
   soil={
    "Alluvial": ["Rice","Wheat","Bajra","Jowar","Soyabean","Linseed","Maize","Potato","Sugarcane"],
    "Black": "Cotton",
    "Read": "Rice",
    "Laterite": "Coconut",
    "Arid": "Maize",
    "Mountain": "Tea",
    "Desert": "Millet",
  }
   print(area)
   print(district)

   le = LabelEncoder()
   le1 = LabelEncoder()
   scaler = load(open("C:\\Users\\HP\\Desktop\\raghav\\mysite\\SIH\\modelml\\scaler.pkl", "rb"))
   le.classes_ = np.load(open("C:\\Users\\HP\\Desktop\\raghav\\mysite\\SIH\\modelml\\en.npy", "rb"), allow_pickle=True)
   le1.classes_ = np.load(open("C:\\Users\\HP\\Desktop\\raghav\\mysite\\SIH\\modelml\\en1.npy", "rb"), allow_pickle=True)
   model = load(open("C:\\Users\\HP\\Desktop\\raghav\\mysite\\SIH\\modelml\\modelrandom.pkl", "rb"))


   p=soil["Alluvial"]
   for i in range(len(p)):
      c=p[i]
      x=[[district,c,area,temp]]
      x=pd.DataFrame(x)
      x=x.values
      x[:,0] = le.transform(x[:,0])
      x[:,1] = le1.transform(x[:,1])
      x=np.array(list(x[:, :]), dtype=np.float)
      x = scaler.transform(x)
      ypred123=model.predict(x)
      ypred[c]=ypred123

   print('ypred')
   ypred1=sorted(ypred.items(), key = lambda kv:(kv[1], kv[0]))
   ypred1.reverse()
   ypred2=ypred1
   while len(ypred1)>5:
       ypred1.pop()

   sale=ypred1
   print(ypred1)
   cn1=ypred1[0][0]
   c1=ypred1[0][1][0]
   cn2=ypred1[1][0]
   c2=ypred1[1][1][0]
   cn3=ypred1[2][0]
   c3=ypred1[2][1][0]
   cn4=ypred1[3][0]
   c4=ypred1[3][1][0]
   d = {"notes":notes,"notes1":notes1,"cnp1":cn1,"cp1":c1,"cnp2":cn2,"cp2":c2,"cnp3":cn3,"cp3":c3,"cnp4":cn4,"cp4":c4,"area":area}
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

def profile(request):
   return render(request,'profile.html')

def fertilizer(request):
   return render(request,'fertilizer.html')


def crop(request):
   allcrop = Crop.objects.all()
   d = {"allcrop":allcrop}

   return render(request,'crop.html',d)

def crop_details(request, cid):
   allcrop = Crop.objects.get(id=cid)
   d = {"cropdetails":allcrop}
   return render(request,'cropdetail.html', d)



def pest_data(request):
   allpest = pest.objects.all()
   d = {"allpest":allpest}

   return render(request,'pest .html',d)

def pest_details(request, pid):
   allpest = pest.objects.get(id=pid)
   data = Pestsolution.objects.filter(pest_name = allpest).first()
   d = {"pest":data}

   return render(request,'pestdetail.html',d)


def Soil_details(request):
    if request.method == "POST":
         d = request.POST
         s = d['sname']
         ph = d['Ph']
         Cn = d['cn']
         Phos = d['phos']
         pot = d['potas']
         soil_detail.objects.create(sname = s,ph = Ph, Cn = cn,Phos = phos,pot = potas)
         return render(request,'home.html',d)
def Add():
    s = "Agar_Malwa Alirajpur Anuppur Ashoknagar Balaghat Barwani Betul Bhind Bhopal Burhanpur Chhatarpur Chhindwara Damoh Datia Dewas Dhar Dindori East_Nimar Guna Gwalior Harda Hoshangabad Indore Jabalpur Jhabua Katni Mandla Mandsaur Morena Narsinghpur Neemuch Panna Raisen Rajgarh Ratlam Rewa Sagar Satna Sehore Seoni Shahdol Shajapur Sheopur Shivpuri Sidhi Singrauli Tikamgarh Ujjain Umaria Vidisha West_Nimar"
    li = s.split()
    for i in li:
        districs.objects.create(name = i)

def ml():
    model = load("C:\\Users\\HP\\Desktop\\raghav\\mysite\\SIH\\Pickle_RL_Model.pkl")
    model.predict()


'''def index(request):
    if request.method == 'POST':
    udata = User_detail.objects.filter(usr = us).first()

    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+str(udata.dis.name)+'&appid=5015184dd36bd3631658ee1d30f3ec0e').read()
    list_of_data = json.loads(source)
    data = {
        "country_code": str(list_of_data['sys']['country']),
        "coordinate": str(list_of_data['coord']['lon']) + ' '
                    + str(list_of_data['coord']['lat']),
        "temp": int(list_of_data['main']['temp']),
        "pressure": str(list_of_data['main']['pressure']),
        "humidity": str(list_of_data['main']['humidity']),
        }
        AllData((data['temp'],data['pressure'],data['humidity'])

    return render(request, "page.html", data)'''


def send_sms(request):
    alldis = districs.objects.all()
    d= {"alldis":alldis}
    if request.method == "POST":
         dd = request.POST
         idd = dd['did']
         disdata = districs.objects.get(id = idd)
         note = districs_notes.objects.filter(dis = disdata).last()
         userdata = User_detail.objects.filter(dis=disdata)
         mobile_no = []
         for i in userdata:
              mobile_no.append(i.mobile)
         for i in mobile_no:
                authkey = "232419AT2rwRRUo5b77e616" # Your authentication key.

                mobiles = i # Multiple mobiles numbers separated by comma.

                message = note # Your message to send.

                sender = "KSPSIH" # Sender ID,While using route4 sender id should be 6 characters long.

                route = "4" # Define route

                # Prepare you post parameters
                values = {
                          'authkey' : authkey,
                          'mobiles' : mobiles,
                          'message' : message,
                          'sender' : sender,
                          'route' : route
                          }


                url = "http://api.msg91.com/api/sendhttp.php" # API URL

                postdata = urllib.parse.urlencode(values) # URL encoding the data here.
                postdata = postdata.encode('ascii')
                req = urllib2.Request(url, postdata)

                response = urllib2.urlopen(req)

                output = response.read() # Get Response
                print(output)


    return render(request,'select_dis.html',d)

