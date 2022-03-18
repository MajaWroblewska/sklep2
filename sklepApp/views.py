from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, FormView, UpdateView, DeleteView

# import plików
from sklepApp.models import Produkt
from sklepApp.forms import ProduktForm, ProduktSelectForm
from sklepApp.models import Kategoria
from sklepApp.forms import KategoriaForm, KategoriaSelactForm
from sklepApp.models import Email
from sklepApp.forms import EmailForm, EmailSelactForm
from sklepApp.models import Adres
from sklepApp.forms import AdresForm, AdresSelectForm
from sklepApp.models import User
from sklepApp.forms import UserForm, UserSelectForm
# from sklepApp.forms import KoszykInForm

#---------------------------------LOGOWANIE--------------------------------
class MojeLogwanie(LoginView):
    template_name = 'login.html'


# ---------------------------------KATEGORIA--------------------------------
class KategoriaView(View):
    def get(self, request):
        return render(request,
                      template_name='kategoria.html',
                      context={'kategorie': Kategoria.objects.all()}
                      )
class KategoriaFiltrView(View):
    def get(self,request):
        knazwa = Kategoria.objects.all()
        print(len(knazwa))
        # print(knazwa[1])
        for i in range(len(knazwa)):
            kate= knazwa[i]
            # print(dir(knazwa[i]))
        a=[knazwa[i].nazwa for i in range(len(knazwa))]
        print(a)

        return render(request,
                      template_name='kategoria_filtr.html',
                      # context={'produkty': Produkt.objects.filter(kategoria__nazwa__contains='far')})
                      # context={'produkty': Produkt.objects.filter(kategoria__nazwa__contains=f'{a}')})
                      # context={'produkty': Produkt.objects.filter(kategoria__nazwa__in=f'{a}')})
                    context={'produkty': Produkt.objects.filter(kategoria = Kategoria.objects.all()[0])},
        )

class KategoriaCreateView(LoginRequiredMixin, FormView):
    template_name = 'kategoria_create_form.html'
    form_class = KategoriaForm
    success_url = reverse_lazy('kategoria')

    def form_valid(self, form):
        result = super(KategoriaCreateView, self).form_valid(form)

        moje_kategorie = form.cleaned_data
        Kategoria.objects.create(
                                 nazwa = moje_kategorie['nazwa'],
                                 )
        return result


class KategoriaUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'kategoria_form.html'
    model = Kategoria
    form_class = KategoriaForm
    success_url = reverse_lazy('kategoria')


class KategoriaSelectUpdateView(LoginRequiredMixin, FormView):
    template_name = 'kategoria_select_form.html'
    form_class = KategoriaSelactForm
    success_url = reverse_lazy('kategoria')

    def form_valid(self, form):
        result = super(KategoriaSelectUpdateView, self).form_valid(form)

        moje_kategorie = form.cleaned_data
        id_kategoria = moje_kategorie['kategorie'].id
        odp = redirect('kategoria_update', pk=id_kategoria)
        return odp


class KategoriaDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'kategoria_delete_form.html'
    model = Kategoria
    success_url = reverse_lazy('kategoria')


class KategoriaSelectDeleteView(LoginRequiredMixin, FormView):
    template_name = 'kategoria_select_form.html'
    form_class = KategoriaSelactForm
    success_url = reverse_lazy('kategoria')
    # permission_required = 'sklepApp.delete_produkt'

    def form_valid(self, form):
        # result= super().form_valid(form) #! poniżej ok !
        result= super(KategoriaSelectDeleteView, self).form_valid(form)
        moje_kategorie = form.cleaned_data

        id_kategoria = moje_kategorie['kategorie'].id
        odp = redirect('kategoria_delete', pk=id_kategoria)

        return odp


#---------------------------------PRODUKT----------------------------------
class ProduktView(View):
    def get(self,request):
        # zd=Produkt.objects.all()[0].zdjecie
        zd=Produkt.objects.all()[0].zdjecie.path
        print(zd) # ->str -> C:\Users\LucWr\Dysk_Google_Maja\PYTHON\_PYTHON_projekty\sklep\01.jpg

        print(zd[63:]) # -> 01.jpg
        print(zd[-6:]) # -> 01.jpg
        # print(type(zd)) # -> str
        # print(dir(zd))
        # print(dir(Produkt.objects.all()[0]))
        return render(request,
                      template_name='produkt.html',
                      context={'produkty': Produkt.objects.all()},
                      )

# class ProduktCreateView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
class ProduktCreateView(LoginRequiredMixin, FormView):
    template_name = 'produkt_create_form.html'
    form_class = ProduktForm
    success_url = reverse_lazy('produkt')
    # permission_required = 'sklepApp.add_produkt'

    def form_valid(self, form):
        result= super().form_valid(form)
        moj_produkt=form.cleaned_data
        Produkt.objects.create(nazwa= moj_produkt['nazwa'],
                               kategoria= moj_produkt['kategoria'],
                               opis= moj_produkt['opis'],
                               # zdjecie=moj_produkt['zdjecie'],
                               ilosc_w_magazynie=moj_produkt['ilosc_w_magazynie'],
                               cena=moj_produkt['cena'],
                               data_dodania=moj_produkt['data_dodania'],
                               data_modyfikacji=moj_produkt['data_modyfikacji']
                               )
        return result

# class ProduktUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
class ProduktUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'produkt_form.html'
    model = Produkt
    form_class = ProduktForm
    success_url = reverse_lazy('produkt')
    permission_required = 'sklepApp.change_produkt'


# class ProduktSelectUpdateView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
class ProduktSelectUpdateView(LoginRequiredMixin, FormView):
    template_name = 'produkt_select_form.html'
    form_class = ProduktSelectForm
    success_url = reverse_lazy('produkt')
    permission_required = 'sklepApp.change_produkt'


    def form_valid(self, form):
        result = super().form_valid(form)

        moje_produkty = form.cleaned_data   #to dict o key='produkt1' z klasy formularza
        id_produkt = moje_produkty['produkty'].id
        # print(id_produkt)

        response = redirect('produkt_update', pk=id_produkt)    #przekierowanie do name url i przekazanie zmiennek <pk>
        return response


# class ProduktDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):
class ProduktDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'produkt_delete_form.html'
    model = Produkt
    success_url = reverse_lazy('produkt')
    permission_required = 'sklepApp.delete_produkt'


# class ProduktSelectDeleteView(PermissionRequiredMixin, LoginRequiredMixin, FormView):
class ProduktSelectDeleteView(LoginRequiredMixin, FormView):
    template_name = 'produkt_select_form.html'
    form_class = ProduktSelectForm
    success_url = reverse_lazy('produkt')
    permission_required = 'sklepApp.delete_produkt'

    def form_valid(self, form):
        # result= super().form_valid(form) #! poniżej ok !
        result= super(ProduktSelectDeleteView, self).form_valid(form)
        moje_produkty = form.cleaned_data

        id_produkt = moje_produkty['produkty'].id
        odp = redirect('produkt_delete', pk=id_produkt)

        return odp

#---------------------------------EMAIL------------------------------------

class EmailView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request,
                      template_name='email.html',
                      context={'emaile': Email.objects.all()}
                      )


class EmailCreateView(LoginRequiredMixin, FormView):
    template_name = 'email_create_form.html'
    form_class = EmailForm
    success_url = reverse_lazy('email')

    def form_valid(self, form):
        result = super(EmailCreateView, self).form_valid(form)

        moje_email = form.cleaned_data
        Email.objects.create(
                             email = moje_email['email'],
                             )
        return result


class EmailUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'email_form.html'
    model = Email
    form_class = EmailForm
    success_url = reverse_lazy('email')


class EmailSelectUpdateView(LoginRequiredMixin, FormView):
    template_name = 'email_select_form.html'
    form_class = EmailSelactForm
    success_url = reverse_lazy('email')

    def form_valid(self, form):
        result = super(EmailSelectUpdateView, self).form_valid(form)

        moje_email = form.cleaned_data
        id_email = moje_email['email'].id
        odp = redirect('email_update', pk=id_email)
        return odp


class EmailDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'email_delete_form.html'
    model = Email
    success_url = reverse_lazy('email')


class EmailSelectDeleteView(LoginRequiredMixin, FormView):
    template_name = 'email_select_form.html'
    form_class = EmailSelactForm
    success_url = reverse_lazy('kategoria')
    # permission_required = 'sklepApp.delete_produkt'

    def form_valid(self, form):
        # result= super().form_valid(form) #! poniżej ok !
        result= super(EmailSelectDeleteView, self).form_valid(form)
        moje_email = form.cleaned_data

        id_email = moje_email['email'].id
        odp = redirect('email_delete', pk=id_email)

        return odp

#---------------------------------ADRES------------------------------------
class AdresView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request,
                      template_name='adres.html',
                      context={'adresy': Adres.objects.all()}
                      )


class AdresCreateView(LoginRequiredMixin, FormView):
    template_name = 'adres_create_form.html'
    form_class = AdresForm
    success_url = reverse_lazy('adres')

    def form_valid(self, form):
        result = super(AdresCreateView, self).form_valid(form)

        moj_adres = form.cleaned_data
        Adres.objects.create(
                             kraj = moj_adres['kraj'],
                             miasto = moj_adres['miasto'],
                             ulica = moj_adres['ulica'],
                             nr_budynku = moj_adres['nr_budynku'],
                             nr_mieszkania = moj_adres['nr_mieszkania'],
                             )
        return result


class AdresUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'adres_form.html'
    model = Adres
    form_class = AdresForm
    success_url = reverse_lazy('adres')


class AdresSelectUpdateView(LoginRequiredMixin, FormView):
    template_name = 'adres_select_form.html'
    form_class = AdresSelectForm
    success_url = reverse_lazy('adres')

    def form_valid(self, form):
        result = super(AdresSelectUpdateView, self).form_valid(form)

        moje_adresy = form.cleaned_data
        id_adres = moje_adresy['adresy'].id
        odp = redirect('adres_update', pk=id_adres)
        return odp


class AdresDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'adres_delete_form.html'
    model = Adres
    success_url = reverse_lazy('adres')


class AdresSelectDeleteView(LoginRequiredMixin, FormView):
    template_name = 'adres_select_form.html'
    form_class = AdresSelectForm
    success_url = reverse_lazy('adres')
    # permission_required = 'sklepApp.delete_adres'

    def form_valid(self, form):
        result= super(AdresSelectDeleteView, self).form_valid(form)
        moje_adresy = form.cleaned_data

        id_adres = moje_adresy['adresy'].id
        odp = redirect('adres_delete', pk=id_adres)

        return odp

#---------------------------------USER-------------------------------------
class UserView(FormView):
    def get(self,request):
        return render (request,
                       template_name='user.html',
                       context= {'usery': User.objects.all()}
                       )


class UserCreateView(LoginRequiredMixin, FormView):
    template_name = 'user_create_form.html'
    form_class = UserForm
    success_url = reverse_lazy('user')

    def form_valid(self, form):
        result = super(UserCreateView, self).form_valid(form)

        moj_user = form.cleaned_data
        User.objects.create(
            imie=moj_user['imie'],
            nazwisko=moj_user['nazwisko'],
            login=moj_user['login'],
            email=moj_user['email'],
            adres=moj_user['adres'],
        )
        return result

class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'user_form.html'
    model = User
    form_class = UserForm
    success_url = reverse_lazy('user')

class UserSelectUpdateView(LoginRequiredMixin, FormView):
    template_name = 'user_select_form.html'
    form_class = UserSelectForm
    success_url = reverse_lazy('user')

    def form_valid(self, form):
        result = super(UserSelectUpdateView, self).form_valid(form)

        moj_user = form.cleaned_data
        id_user = moj_user['usery'].id
        odp = redirect('user_update', pk=id_user)
        return odp

class UserDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'user_delete_form.html'
    model = User
    success_url = reverse_lazy('user')

class UserSelectDeleteView(LoginRequiredMixin, FormView):
    template_name = 'user_select_form.html'
    form_class = UserSelectForm
    success_url = reverse_lazy('user')

    # permission_required = 'sklepApp.delete_user'

    def form_valid(self, form):
        result = super(UserSelectDeleteView, self).form_valid(form)
        moj_user = form.cleaned_data

        id_user = moj_user['usery'].id
        odp = redirect('user_delete', pk=id_user)

        return odp

#---------------------------------KOSZYK_LOGIN-----------------------------







#---------------------------------KOSZYK_LOGOUT----------------------------

#--------------------------------------------------------------------------
#autoryzacja (Produkt, Kategoria, Email, Adres, User, Koszyk_login, Koszyk_logout, ) -

# ( Koszyk_login, Koszyk_logout), + widok
# ( Koszyk_login, Koszyk_logout), + formularz
# ( Koszyk_login, Koszyk_logout), + update i delete
# ( Koszyk_login, Koszyk_logout), + select do update i delete
# ( Koszyk_login, Koszyk_logout), + autentykacja
