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

menuList = [("/", "Accueil"), ("/Membres/", "Membres"), ("/Defis/", "Défis"), ("/Video/", "Vidéo"), ("/Voyage/", "Voyages"), ("/Sponsors/", "Sponsors"), ("/Event/", "Événement")]

sponsorList = [("Lyf Pay", "sponso/lyf.png", "Lyf pay est trop bien"), ("Ornikar", "sponso/ornikar.jpg", "Ornikar est trop cool"), ("Vapiano", "sponso/vapiano.png", "Resto italiano"), 
("StaffMe", "sponso/staffme.png", "surprise pour la journée de campagne"), ("Onyxia", "sponso/Onyxia.png", "sushi!"), ("Zozan", "sponso/Zozan.png", "La boisson est offerte"), 
("Axel.Le", "sponso/axel le.png", "hmmm essuie fraise"), ("Credit Mutuel", "sponso/cm.png", "Les potos qui gardent notre moula"), ("Lyf Pay", "sponso/lyf.png", "Lyf pay est trop bien"), 
("Lyf Pay", "sponso/lyf.png", "Lyf pay est trop bien")]

voyageList = [("wei", "Week-End d'Intégration", "Inconnu", "Ce week-end iconique permet de faire connaissance et d'intégrer les personnes venant de prépa, mais aussi pour finir sur une bonne note ton été 2K22, au programme : Soirée, piscine, Jeux, bonne ambiance… Tous les éléments sont réunis pour te faire kiffer."), 
("ski", "Semaine de Ski", "Serre chevalier Valée", "En plein milieu des Hautes-Alpes, Nous nous engageons à t'offrir le meilleur voyage de ski qui existe. 250 km de pistes avec une vue sur le massif des Écrins, une semaine avec une prestation All Inclusive, t'as juste à faire ton sac et n'oublie pas ton bonnet !!"), 
("europe", "Voyage en Europe", "Naples", "Hydra vous donne rdv en Italie pour faire trembler le volcan caché sous cette charmante ville, Soirée privée, Boîtes de nuit, restaurants italien, Apéro, soleil, Activités. Prépare toi car tu vas peut-être oublier de dormir.")]

eventList = [("Allôs", "Lundi 21 février 2022", "De 16h à minuit, nous pouvons vous livrer quasiment tout ce qui vous passe par la tête. Vous avez une petite faim ? Vous prévoyez un apéro ? Vous avez envie de vous tester au yoga ?", "Le détails arrivera sous peu, on va pas tout vous dire maintenant voyons..."),
("Petit déjeuner", "Vendredi 25 février 2022", "Vos placards sont vides ? Vous rentrez de soirée et vous avez faim ? Venez manger une bonne viennoiserie, ou une bonne crêpe, en notre compagnie. Bien évidemment on n'a ni oublié le café ni le thé...", ""),
("Journée de campagne", "Mercredi 9 mars 2022", "Vous l'attendiez tous. La journée la plus attendue de l'année. Au programme ? Dès 6h, un petit déjeuner vous attendra pour vous remettre de la veille. Tout au long de la journée, diverses activités dont un certain mariage... vous feront patienter jusqu'à une na'incroyable soirée !", "C'est la journée la plus importante de l'année, il faut garder un peu de surprise voyons..."),
("Afterwork", "Lundi 14 mars 2022", "Fatigué d'une journée de cours ? Ras le bol du début de semaine au travail ? Vient te détendre avec nous en buvant une bonne pinte de bière bien raffraîchissante.", "Dans la salle du Au Coin! Dès 18h")]

def Defis(request):
    
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
            if defi.val()["titre"] != "AFCSGHDFHJW":
                idlist.append(defi.val()["count"])
                desclist.append(defi.val()["desc"])
                titrelist.append(defi.val()["titre"])
                donneurlist.append(defi.val()["donneur"])
                datelist.append(defi.val()["date"])
    
    for i in idlist:
        dictdefi={'id':idlist[c],'titre':titrelist[c],'desc':desclist[c],'date':datelist[c],'donneur':donneurlist[c]}
        c+=1
        final.append(dictdefi)
    


    #Done:
    all_done = database.child("done").get()
    

    iddone=[]
    donelist=[]
    titredone=[]
    descdone=[]
    datedone=[]
    donneurdone=[]
    for defi in all_done:
       
        if defi.val()["titre"] != "AFCSGHDFHJW":
            iddone.append(defi.val()['donecount'])
            descdone.append(defi.val()["desc"])
            titredone.append(defi.val()["titre"])
            donneurlist.append(defi.val()["donneur"])
            datedone.append(defi.val()["datedone"])
    
    for c in range(len(iddone)):
        dictdone={'id':iddone[c],'titre':titredone[c],'desc':descdone[c],'date':datedone[c],'donneur':donneurlist[c]}
        donelist.append(dictdone)
    
    if request.method == 'POST':
        if request.POST.get("submit"):
            
            
            form = NameForm(request.POST)
            
            if form.is_valid():
                titre=form.cleaned_data.get('titre')
                
                donneur = form.cleaned_data.get('donneur')
                
                desc=form.cleaned_data.get('desc')
                print("testsetest")
                print(titre, desc, donneur)

                data={"titre":titre, "desc":desc, "date":str(datetime.datetime.now()), "donenu":-1, "lienvid":"lien", "donneur":donneur,"count":database.child("count").get().val()}
                n='defi{}'.format(database.child("count").get().val())
                database.child("defis").child(n).set(data)  
                
                vaniquertamere = int(database.child("count").get().val())
                database.child("count").set(vaniquertamere+1)
        return HttpResponseRedirect("/Defis")

   
    return render(request, 'Defis.html', {'form': form ,'final':final,'donelist':donelist, 'menuList': menuList})

def Acceuil(request):
    return render(request,'Acceuil.html',{})

def Accueil(request):
    return render(request,'Accueil.html',{'menuList': menuList})

def Membres(request):
    return render(request,'Membres.html',{'menuList': menuList})

def Sponsors(request):
    return render(request,'Sponsors.html',{'menuList': menuList, 'sponsorList': sponsorList})

def Video(request):
    return render(request,'Video.html', {'menuList': menuList})

def Voyage(request):
    return render(request,'Voyage.html',{'menuList': menuList, 'voyageList':voyageList})

def Event(request):
    return render(request,'Event.html',{'menuList': menuList, 'eventList':eventList})

