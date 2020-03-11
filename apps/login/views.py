from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import  SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views.generic import CreateView
# Create your views here.

class Register(CreateView):
    model = User
    template_name = "Login/Register.html"
    form_class = SignUpForm
    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        sucess_url = "../"
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        try:
            if self.request.user.is_authenticated:
                return redirect(sucess_url)
            #Sino lo está entonces nos muestra la plantilla del login simplemente
            else:
                return redirect('/AdminLogin')
        except:
            return redirect('/AdminLogin')
class Login(FormView):
    #Establecemos la plantilla a utilizar
    template_name = 'Login/Login.html'
    #Le indicamos que el formulario a utilizar es el formulario de autenticación de Django
    form_class = AuthenticationForm
    #Le decimos que cuando se haya completado exitosamente la operación nos redireccione a la url bienvenida de la aplicación personas
    success_url =  '../'
    def dispatch(self, request, *args, **kwargs):
        #Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
        try:
            if request.user.is_authenticated():
                return HttpResponseRedirect(self.success_url())
            #Sino lo está entonces nos muestra la plantilla del login simplemente
            else:
                return super(Login, self).dispatch(request, *args, **kwargs)
        except:
            return super(Login, self).dispatch(request, *args, **kwargs)
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)