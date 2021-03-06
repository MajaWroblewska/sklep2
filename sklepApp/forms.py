# formularze do modeli
from django import forms
from django.forms import Textarea

from sklepApp.models import Kategoria, Produkt, Email, Adres, User


#---------------------------------KATEGORIA--------------------------------
class KategoriaForm(forms.ModelForm):
    class Meta:
        model = Kategoria
        fields = '__all__'
    nazwa = forms.CharField(max_length=100)


class KategoriaSelactForm(forms.Form):
    kategorie= forms.ModelChoiceField(queryset=Kategoria.objects)


#---------------------------------PRODUKT----------------------------------
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Niebieski'),
    ('green', 'Zielony'),
    ('black', 'Czarny'),
    ('red', 'DUPA')
]
MC=['styczen', 'luty', 'marzec', 'kwiecień', 'maj', 'czerwiec', 'lipiec', 'sierpień', 'wrzesień', 'październik', 'listopad', 'grudzień']
# MIESIACE={'1':'styczen', '2':'luty', '3':'marzec', '4':'kwiecien'}
MIESIACE = {str(lp):value   for lp, value in enumerate(MC)}
class ProduktForm(forms.ModelForm):
    class Meta:
        model= Produkt
        # fields= '__all__'
        exclude= ['data_dodania','data_modyfikacji']

    nazwa = forms.CharField(max_length=200)
    kategoria = forms.ModelChoiceField(queryset=Kategoria.objects)
    opis = forms.CharField(widget=Textarea)
    zdjecie = forms.ImageField(allow_empty_file=True, required=False)
    ilosc_w_magazynie = forms.IntegerField(min_value=0)
    cena = forms.DecimalField(min_value=0, max_digits=10, decimal_places=2)
    data_dodania = forms.DateTimeField(widget = forms.SelectDateWidget)
    data_modyfikacji = forms.DateTimeField(widget = forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, months=MIESIACE))

    # data_modyfikacji = forms.MultipleChoiceField(required=False,
    #                                              widget=forms.CheckboxSelectMultiple,
    #                                              choices=FAVORITE_COLORS_CHOICES,
    #                                              )


class ProduktSelectForm(forms.Form):
    produkty= forms.ModelChoiceField(queryset=Produkt.objects)

#---------------------------------EMAIL------------------------------------
class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
        # exclude = ['email']
    email = forms.EmailField()


class EmailSelactForm(forms.Form):
    email= forms.ModelChoiceField(queryset=Email.objects)
#---------------------------------ADRES------------------------------------

class AdresForm(forms.ModelForm):
    class Meta:
        model = Adres
        fields = "__all__"
        # exclude = ['nr_mieszkania']
    kraj = forms.CharField(max_length=100)
    miasto = forms.CharField(max_length=100)
    ulica = forms.CharField(max_length=100)
    nr_budynku = forms.IntegerField(min_value=1)
    nr_mieszkania = forms.IntegerField(min_value=1)


class AdresSelectForm(forms.Form):
    adresy = forms.ModelChoiceField(queryset=Adres.objects)

#---------------------------------USER-------------------------------------
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        # exclude = ['adres']
    imie = forms.CharField(max_length=100)
    nazwisko = forms.CharField(max_length=200)
    login = forms.CharField(max_length=100)
    email = forms.ModelChoiceField(queryset=Email.objects)
    adres = forms.ModelChoiceField(queryset=Adres.objects)


class UserSelectForm(forms.Form):
    usery = forms.ModelChoiceField(queryset=User.objects)

#---------------------------------KOSZYK_LOGIN-----------------------------



#---------------------------------KOSZYK_LOGOUT----------------------------
