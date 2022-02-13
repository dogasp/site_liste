from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
import pyrebase
from .forms import NameForm
import datetime

config={
  "apiKey": "AIzaSyAI0KK-ff21JLuLIDhVbBcwfDh63HfoDCY",
  "authDomain": "site-liste-hydra-e6a25.firebaseapp.com",
  "projectId": "site-liste-hydra-e6a25",
  "storageBucket": "site-liste-hydra-e6a25.appspot.com",
  "messagingSenderId": "809157089116",
  "appId": "1:809157089116:web:a45f65cdcb6f2aff409399",
  "measurementId": "G-VQ33YWV56V",
  "databaseURL" : "https://site-liste-hydra-e6a25-default-rtdb.europe-west1.firebasedatabase.app/"
}


    

def defis(request):
    
    firebase=pyrebase.initialize_app(config)
    authe = firebase.auth()
    database=firebase.database()
    form = NameForm(request.POST)
     #va chercher les données de la Db et les affiche dans un tableau dans defis.html
    
    all_defis = database.child("defis").get()
    defilist=[]
    for defi in all_defis:
        if defi.key() != 'count' :
            if defi.val()["titre"] != "test":
                defilist.append(defi.val())
   
   

    if request.method == 'POST':
        if request.POST.get("submit"):
            print("submit")
            
            form = NameForm(request.POST)
   
            if form.is_valid():
                titre=form.cleaned_data.get('titre')
               

                desc=form.cleaned_data.get('desc')
                
                
               
                data={"titre":titre, "desc":desc, "date":str(datetime.datetime.now()), "donenu":-1, "lienvid":"lien", "donneur":"donneur","count":len(database.child('defis').get().val())}
                n='defi{}'.format(database.child("count").get().val())
                database.child("defis").child(n).set(data)  
                
                vaniquertamere = int(database.child("count").get().val())
                database.child("count").set(vaniquertamere+1)
        return HttpResponseRedirect("/defis")

   
    return render(request, 'defis.html', {'form': form ,'defis':defilist})
def Acceuil(request):
    
    return render(request,'Acceuil.html',{})


def membres(request):
    return render(request,'membres.html',{})

def sponsors(request):
    return render(request,'sponsors.html',{})

def video(request):
    return render(request,'video.html',{})

def voyage(request):
    return render(request,'voyage.html',{})


