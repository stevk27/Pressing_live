from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Module client 

class Adresse_local(models.Model):
    ville = models.charField(max_length = 100, blank = True, null = True)
    quartier = models.charField(max_length = 100, blank = True, null = True)
    description = models.TextField(max_length = 300, blank = True, null = True)

    def __str__(self):
        return self.ville

class Adresse_geographique(models.Model):
    longitude = models.DecimalField()
    latitude =  models.DecimalField()
    

class Client(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    prenom  = models.charField(max_length = 100, null = True, blank = True)
    telephone = models.charField(max_length = 100, null = True, blank = True)
    adresse_geographique = models.ForeignKey(Adresse_geographique, on_delete = models.CASCADE, blank = True)
    adresse_locale = models.ForeignKey(Adresse_local, on_delete=models.CASCADE, null = True , blank = True)
    
    def __str__(self):

        return self.prenom

class Localisation_pressing(models.Model):
    longitude = models.DecimalField()
    latitude =  models.DecimalField()
     
class Adresse_pressing(models.Model):
    ville = models.CharField(max_length = 100, null =  True, blank = True)
    quartier = models.CharField(max_length = 100, null = True , blank = True)
    Bp = models.CharField(max_length = 10, null = True , blank = True)


class Pressing(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    enseigne_juridique = models.charField(max_length = 100)
    numero_imatriculation = models.charField(max_length =  100, null = True, blank = True)
    telephone = models.CharField(max_length = 10, null = True , blank = True)

    def __str__(self):
        return self.enseigne_juridique



class Categorie_Article(models.Model):
    pass


class Article(models.Model):
    pass    









