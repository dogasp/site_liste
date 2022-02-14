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

menuList = [("/", "Accueil"), ("/Membres/", "Membres"), ("/Defis/", "Défis"), ("/Video/", "Vidéo"), ("/Voyage/", "Voyages"), ("/Sponsors/", "Sponsors"), ("/Event/", "Événement")]

sponsorList = [("Lyf Pay", "sponso/lyf.png", "Lyf pay est trop bien"), ("Ornikar", "sponso/ornikar.jpg", "Ornikar est trop cool"), ("Lyf Pay", "sponso/lyf.png", "Lyf pay est trop bien"), 
("Lyf Pay", "sponso/lyf.png", "Lyf pay est trop bien"), ("Lyf Pay", "sponso/lyf.png", "Lyf pay est trop bien"), ("Lyf Pay", "sponso/lyf.png", "Lyf pay est trop bien"), 
("Lyf Pay", "sponso/lyf.png", "Lyf pay est trop bien"), ("Lyf Pay", "sponso/lyf.png", "Lyf pay est trop bien"), ("Lyf Pay", "sponso/lyf.png", "Lyf pay est trop bien"), 
("Lyf Pay", "sponso/lyf.png", "Lyf pay est trop bien")]

voyageList = [("wei", "Week-End d'Intégration", "Inconnu", "Le wei sera juste génial"), ("ski", "Semaine de Ski", "Serre chevalier Valée", "Une des meilleures stations de France"), ("europe", "Voyage en Europe", "Naples", "Sur les traces de la mafia italienne")]

def Defis(request):
    
    firebase=pyrebase.initialize_app(config)
    authe = firebase.auth()
    database=firebase.database()
    form = NameForm(request.POST)
     #va chercher les données de la Db et les affiche dans un tableau dans defis.html
    
    all_defis = database.child("defis").get()
    defilist=[]
    for defi in all_defis:
        if defi.val()["titre"] != "test":
            defilist.append(defi.val())
   
    if request.method == 'POST':
        if request.POST.get("submit"):
            print("submit")
            
            form = NameForm(request.POST)
   
            if form.is_valid():
                titre=form.cleaned_data.get('titre')
               

                desc=form.cleaned_data.get('desc')
                
                
               
                data={"titre":titre, "desc":desc, "date":str(datetime.datetime.now())}
                n='defi{}'.format(len(database.child('defis').get().val()))
                database.child("Defis").child(n).set(data)  
 
        return HttpResponseRedirect("/Defis")

   
    return render(request, 'Defis.html', {'form': form ,'defis':defilist, 'menuList': menuList})

def Accueil(request):
    return render(request,'Accueil.html',{'menuList': menuList})

def Membres(request):
    return render(request,'Membres.html',{'menuList': menuList})

def Sponsors(request):
    return render(request,'Sponsors.html',{'menuList': menuList, 'sponsorList': sponsorList})

def Video(request):
    return render(request,'Video.html',{'menuList': menuList})

def Voyage(request):
    return render(request,'Voyage.html',{'menuList': menuList, 'voyageList':voyageList})

def Event(request):
    return render(request,'Event.html',{'menuList': menuList})

