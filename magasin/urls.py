from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import ContactView

urlpatterns = [ 
    path('', views.index, name='index'),
    path('neveauProduit/', views.nouveauProduit, name='ajoutProduit'),
    path('nouvFournisseur/',views.nouveauFournisseur,name='nouveauFour'),
   
    path('listFournisseur/',views.listFournisseur,name='listFour'),
    path('nouvCommande/',views.nouveauCommande,name='nouveauCommande'),
    path('contact/', ContactView.as_view(), name='contact'),
 
    
    path('register/',views.register, name = 'register'),

]