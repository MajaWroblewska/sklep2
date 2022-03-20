"""DjangoSklep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from sklepApp.views import MojeLogwanie
from sklepApp.views import (ProduktView, ProduktCreateView, ProduktUpdateView, ProduktDeleteView, \
    ProduktSelectUpdateView, ProduktSelectDeleteView )
from sklepApp.views import (KategoriaView, KategoriaCreateView, KategoriaUpdateView, KategoriaDeleteView, \
    KategoriaSelectUpdateView, KategoriaSelectDeleteView)
from sklepApp.views import EmailView, EmailCreateView, EmailUpdateView, EmailDeleteView, \
    EmailSelectUpdateView, EmailSelectDeleteView
from sklepApp.views import AdresView, AdresCreateView, AdresUpdateView, AdresDeleteView, \
    AdresSelectUpdateView, AdresSelectDeleteView
from sklepApp.views import UserView, UserCreateView, UserUpdateView,UserDeleteView, \
    UserSelectUpdateView, UserSelectDeleteView
# from sklepApp.views import Koszyk_loginView, Koszyk_loginCreateView
from sklepApp.views import KategoriaFiltrSelectView, Filtr
from sklepApp.views import Dodaj_do_koszyka

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', MojeLogwanie.as_view(), name='login'),

    path('produkt/', ProduktView.as_view(), name='produkt'),
    path('produkt/create', ProduktCreateView.as_view(), name='produkt_create'),
    path('produkt/update/<pk>', ProduktUpdateView.as_view(), name='produkt_update'),
    path('produkt/update', ProduktSelectUpdateView.as_view(), name='select_produkt_update'),
    path('produkt/delete/<pk>', ProduktDeleteView.as_view(), name='produkt_delete'),
    path('produkt/delete/', ProduktSelectDeleteView.as_view(), name='select_produkt_delete'),
    path('produkt/dodaj/<pk>', Dodaj_do_koszyka.as_view(), name='dodaj_do_koszyka'),

    path('kategoria/', KategoriaView.as_view(), name='kategoria'),
    path('kategoria/create', KategoriaCreateView.as_view(), name='kategoria_create'),
    path('kategoria/update/<pk>', KategoriaUpdateView.as_view(), name='kategoria_update'),
    path('kategoria/update', KategoriaSelectUpdateView.as_view(), name='select_kategoria_update'),
    path('kategoria/delete/<pk>', KategoriaDeleteView.as_view(), name='kategoria_delete'),
    path('kategoria/delete/', KategoriaSelectDeleteView.as_view(), name='select_kategoria_delete'),
    path('kategoria/filtr/', KategoriaFiltrSelectView.as_view(), name='select_kategoria_filtr'),
    path('kategoria/filtr/<pk>', Filtr.as_view(), name='kategoria_filtr'),

    path('email/', EmailView.as_view(), name='email'),
    path('email/create', EmailCreateView.as_view(), name='email_create'),
    path('email/update/<pk>', EmailUpdateView.as_view(), name='email_update'),
    path('email/update', EmailSelectUpdateView.as_view(), name='select_email_update'),
    path('email/delete/<pk>', EmailDeleteView.as_view(), name='email_delete'),
    path('email/delete', EmailSelectDeleteView.as_view(), name='select_email_delete'),

    path('adres/', AdresView.as_view(), name='adres'),
    path('adres/create', AdresCreateView.as_view(), name='adres_create'),
    path('adres/update/<pk>', AdresUpdateView.as_view(), name='adres_update'),
    path('adres/update', AdresSelectUpdateView.as_view(), name='select_adres_update'),
    path('adres/delete/<pk>', AdresDeleteView.as_view(), name='adres_delete'),
    path('adres/delete', AdresSelectDeleteView.as_view(), name='select_adres_delete'),

    path('user/', UserView.as_view(), name='user'),
    path('user/create', UserCreateView.as_view(), name='user_create'),
    path('user/update/<pk>', UserUpdateView.as_view(), name='user_update'),
    path('user/update', UserSelectUpdateView.as_view(), name='select_user_update'),
    path('user/delete/<pk>', UserDeleteView.as_view(), name='user_delete'),
    path('user/delete', UserSelectDeleteView.as_view(), name='select_user_delete'),

    # # path('koszykin/', Koszyk_loginView.as_view(), name= 'koszyk_login'),
    # # path('koszykin/create', Koszyk_loginCreateView.as_view(), name= 'koszyk_login_create'),
]
