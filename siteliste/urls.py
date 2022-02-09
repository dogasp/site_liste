from django.conf import settings
from django.urls import path
from siteliste import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Acceuil, name='Acceuil'),
    path('defis/', views.defis, name='defis'),
    path('membres/', views.membres, name='membres'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('video/', views.video, name='video'),
    path('voyage/', views.voyage, name='voyage'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
