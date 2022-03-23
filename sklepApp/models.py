from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

# ---------------------------------KATEGORIA--------------------------------
class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nazwa}'


#---------------------------------PRODUKT----------------------------------
class Produkt(models.Model):
    nazwa = models.CharField(max_length=200)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    opis = models.TextField(default='opis_domyślny')
    zdjecie = models.ImageField(upload_to='images/', default='static/27.jpg', null=True, blank=True)
    ilosc_w_magazynie = models.IntegerField(default=0)
    cena = models.DecimalField(max_digits=7, decimal_places=2, default=1.00)
    data_dodania = models.DateTimeField(auto_now_add=True)  # podczas tworzenia
    data_modyfikacji = models.DateTimeField(auto_now=True)  # przy zapisie

    def __str__(self):
        return f'{self.nazwa} : img={self.zdjecie} : stan={self.ilosc_w_magazynie} : cena= {self.cena}'  # : data dod/mod= {self.data_dodania}/{self.data_modyfikacji}'


#---------------------------------EMAIL------------------------------------

class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return f'{self.email}'


#---------------------------------ADRES------------------------------------

class Adres(models.Model):
    kraj = models.CharField(max_length=100)
    miasto = models.CharField(max_length=100)
    ulica = models.CharField(max_length=100)
    nr_budynku = models.IntegerField()
    nr_mieszkania = models.IntegerField()

    def __str__(self):
        return f'{self.id} {self.kraj}-{self.miasto}-{self.ulica}-{self.nr_budynku}/{self.nr_mieszkania}'


#---------------------------------USER-------------------------------------
class User(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=200)
    login = models.CharField(max_length=100)
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    adres = models.ForeignKey(Adres, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.imie} {self.nazwisko} - {self.login}'


#---------------------------------KOSZYK_LOGIN-----------------------------




#---------------------------------KOSZYK_LOGOUT----------------------------



# -------------------------------------------------------------------------------

