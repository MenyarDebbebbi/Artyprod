from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib import messages
from magasin.forms import serviceForm,FournisseurForm,CommandeForm,UserRegistrationForm
from .models import Produit,Fournisseur,Commande,Project,Service,BlogPost
from django.contrib.auth.decorators import login_required
from django.views import View

def aaa(request):
    template=loader.get_template('magasin/service.html')
    projects= Project.objects.all()
    context={'projects': projects}
    return render( request,'magasin/mesProjects.html',context )

@login_required
def index(request):
    if request.method == "POST" : 
        form = serviceForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('magasin/')
    else :
        form = serviceForm()
        list=BlogPost.objects.all()
    return render(request,'magasin/vitrine.html',{'list':list,'form':form})

@login_required
def nouveauProduit(request):
    if request.method == "POST" : 
        form = serviceForm(request.POST,request.FILES)
        return HttpResponseRedirect('/magasin')
    else :
        list=Service.objects.all()
    return render(request,'magasin/service.html',{'list':list})

@login_required
def listFournisseur(request):
    if request.method == "POST" : 
        form = FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/nouvFournisseur')
    else :
        form = FournisseurForm()
        list=Project.objects.all()
    return render(request,'magasin/project.html',{'list':list,'form':form})

@login_required
def nouveauFournisseur(request):
    if request.method == "POST" : 
        form = FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/nouvFournisseur')
    else :
        form = FournisseurForm()
        list=Fournisseur.objects.all()
    return render(request,'magasin/ajoutFournisseur.html',{'list':list,'form':form})


@login_required
def nouveauCommande(request):
    if request.method == "POST" : 
        form = CommandeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/nouvFournisseur')
    else :
        form = CommandeForm()
        list=Commande.objects.all()
    return render(request,'magasin/project.html',{'list':list,'form':form})

def register(request):
    if request.method == 'POST' :
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return HttpResponseRedirect('/magasin')
    else :
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form' : form})




class ContactView(View):
    def get(self, request):
        return render(request,'magasin/contact.html')
