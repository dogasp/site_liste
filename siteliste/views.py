from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
import numpy
import pyrebase
from .forms import NameForm
import datetime
from numpy import array

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
    c=0
    idlist=[]
    final=[]
    titrelist=[]
    desclist=[]
    datelist=[]
    donneurlist=[]
    for defi in all_defis:
        if defi.val()["count"] != 0:
            if defi.val()["titre"] != "test":
                idlist.append(defi.val()["count"])
                desclist.append(defi.val()["desc"])
                titrelist.append(defi.val()["titre"])
                #donneurlist.append(defi.val()["donneur"])
                datelist.append(defi.val()["date"])
   
    for i in idlist:
        dictdefi={'id':idlist[c],'titre':titrelist[c],'desc':desclist[c],'date':datelist[c]}
        c+=1
        final.append(dictdefi)
    


    #Done:
    all_done = database.child("done").get()
    
    c=0
    iddone=[]
    donelist=[]
    titredone=[]
    descdone=[]
    datedone=[]
    donneurdone=[]
    for defi in all_done:
       
        if defi.val()["titre"] != "test" and defi.val()["donecount"] != 0:
            iddone.append(defi.val()["donecount"])
            descdone.append(defi.val()["desc"])
            titredone.append(defi.val()["titre"])
                #donneurlist.append(defi.val()["donneur"])
            datedone.append(defi.val()["datedone"])
    
    for i in iddone:
        dictdone={'id':iddone[c],'titre':titredone[c],'desc':descdone[c],'date':datedone[c]}
        c+=1
        donelist.append(dictdone)
    
    
    
    if request.method == 'POST':
        if request.POST.get("submit"):
            
            
            form = NameForm(request.POST)
            
            if form.is_valid():
                titre=form.cleaned_data.get('titre')
                
                desc=form.cleaned_data.get('desc')
                
                donneur = form.cleaned_data.get('donneur')
                
                print(donneur)

                data={"titre":titre, "desc":desc, "date":str(datetime.datetime.now()), "donenu":-1, "lienvid":"lien", "donneur":"donneur","count":database.child("count").get().val()}
                n='defi{}'.format(database.child("count").get().val())
                database.child("defis").child(n).set(data)  
                
                vaniquertamere = int(database.child("count").get().val())
                database.child("count").set(vaniquertamere+1)
        return HttpResponseRedirect("/defis")

   
    return render(request, 'defis.html', {'form': form ,'final':final,'donelist':donelist})
def Acceuil(request):
    
    return render(request,'Acceuil.html',{})


def membres(request):
    return render(request,'membres.html',{})

def sponsors(request):
    return render(request,'sponsors.html',{})

def video(request):
    afin=[
        { "id":1, "name": "Python", "author":"idk", "copies": 1},
{ "id":2, "name": "Java", "author":"idk2", "copies": 3}

    ]
    print
    return render(request,'video.html',{"afin":afin})

def voyage(request):
    return render(request,'voyage.html',{})


