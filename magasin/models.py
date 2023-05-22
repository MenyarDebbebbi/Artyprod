
from django.db import models
from datetime import date
# Create your models here.

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    is_registered = models.BooleanField(default=False)
     
    @staticmethod
    def get_customer_by_email(email):
        try :
            return User.objects.get(email = email)
        except :
            return False
        
    def register(self) :
        return self.save()
    
    def isExist(self):
        if User.objects.filter(email = self.email):
            return True
        return False

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assigned_team = models.ForeignKey('equipe', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Service(models.Model):
    TYPE_CHOICES = [
        ('Ch', 'Charte Graphique'),
        ('Obj', 'Objet 3D'),
        ('Scé', 'Scénarisation')
    ]

    type = models.CharField(max_length=5, choices=TYPE_CHOICES, default='Obj')
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ManyToManyField(Project, through='Detail')
 
    def __str__(self):
        return self.name
                                


class Detail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file = models.FileField()

class equipe(models.Model):
    name = models.CharField(max_length=100)
    Personnel= models.ManyToManyField('Personnel')

    def __str__(self):
        return self.name

class Personnel(models.Model):
    name = models.CharField(max_length=100)
    Cv=models.ImageField(blank=True)    
    photo=models.ImageField(blank=True)    
    linkedin_profile = models.URLField()

class BlogPost(models.Model):
    img=models.ImageField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Personnel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Categorie(models.Model):
    name=models.CharField(max_length=50,default='Al')
    def __str__(self):
        return self.name


class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return self.nom+" "+self.adresse+" "+self.email+" "+self.telephone

class Produit(models.Model):
    TYPE_CHOICES=[('em','emballé'),('fr','Frais'),('cs','Conserve')]
    libellé=models.CharField(max_length=100)
    description=models.TextField(default='Non définie')
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True)
    catégorie=models.ForeignKey(Categorie,on_delete=models.CASCADE,null=True)
    Fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.libellé+" "+self.description+" "+str(self.prix)

class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return self.Duree_garantie+" "+self.libellé

class ProduitC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return self.Duree_garantie+" "+self.libellé

class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produits=models.ManyToManyField('Produit')
    def __str__(self):
        return str(self.dateCde)+" "+str(self.totalCde)
    
