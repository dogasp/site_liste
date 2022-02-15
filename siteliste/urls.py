from django.conf import settings
from django.urls import path
from siteliste import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Accueil, name='Accueil'),
    path('Defis/', views.Defis, name='Defis'),
    path('Membres/', views.Membres, name='Membres'),
    path('Sponsors/', views.Sponsors, name='Sponsors'),
    path('Video/', views.Video, name='Video'),
    path('Voyage/', views.Voyage, name='Voyage'),
    path('Event/', views.Event, name='Event'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
