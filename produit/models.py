from django.db import models
from categorie.models import Categorie
from vendeur.models import Vendeur

# Create your models here.
class Produit(models.Model):
    nom = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    prix_achat = models.FloatField()
    stock = models.IntegerField(default=0)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    vendeurs = models.ManyToManyField(Vendeur)
    #prix_livraison = models.FloatField()
    marque = models.CharField(max_length=200, null=True)
    image = models.FileField()
    date_creation = models.DateTimeField(auto_now=True, null=True)
    
    
    def __str__(self):
        return self.nom
