from django.contrib import admin
from sklepApp.models import Kategoria, Produkt
from sklepApp.models import Email, Adres, User
# from sklepApp.models import Koszyk_login, Koszyk_logout

# Register your models here.
# admin.site.register(Kategoria)
# admin.site.register(Produkt)
# admin.site.register(Adres)
# admin.site.register(User)
# admin.site.register(Email)
# admin.site.register(Koszyk_logout)
# admin.site.register(Koszyk_login)


@admin.register(Kategoria)
class KategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nazwa']
    search_fields = ('nazwa',) #lista lub tupla
    # list_filter = ('nazwa',) #zbedne


@admin.register(Produkt)
class ProduktAdmin(admin.ModelAdmin):
    list_display = ['id','nazwa','zdjecie','ilosc_w_magazynie', 'cena', 'kategoria','data_dodania','data_modyfikacji' ]
    list_filter = ('kategoria', 'ilosc_w_magazynie','cena','nazwa' )
    search_fields = ('kategoria__nazwa','nazwa',)
    ordering = ['nazwa','id']
    list_editable = ['cena', 'ilosc_w_magazynie']


@admin.register(Adres)
class AdresAdmin(admin.ModelAdmin):
    list_display = ('id','kraj','miasto','ulica', 'nr_budynku', 'nr_mieszkania')
    list_filter = ('kraj','miasto','ulica', 'nr_budynku', 'nr_mieszkania' )
    ordering = ['kraj', 'miasto','ulica','nr_budynku', 'nr_mieszkania','id']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','imie','nazwisko','login', 'adres')
    list_filter = ('imie','nazwisko','login', 'adres')


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ['id', 'email']
    list_filter = ['email']


# @admin.register(Koszyk_login)
# class Koszyk_loginAdmin(admin.ModelAdmin):
#     list_display = ['id', 'nr_zamowienia','user',]
#
#
# @admin.register(Koszyk_logout)
# class Koszyk_logoutAdmin(admin.ModelAdmin):
#     list_display = ['id', 'nr_zamowienia',]

