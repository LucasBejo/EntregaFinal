
from django.shortcuts import render
from django.http import HttpResponse
from App.forms import *
from App.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.


def inicio(request):
    
    return render(request, "App/inicio.html")



@login_required
def datos(request):
    
    if request.method == 'POST':

        miFormulario = DatosFormulario(request.POST)
        
        print(miFormulario)
        
        if miFormulario.is_valid:
            
          informacion = miFormulario.cleaned_data

          datos = Datos (nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'])
        
          datos.save()
        
          return render(request,"App/inicio.html")
    else:
        miFormulario=DatosFormulario()
    
    return render(request,"App/datos.html", {"miFormulario":miFormulario})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data=request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
           
            if user is not None:
                login(request,user)

                return render(request,"App/inicio.html",{"mensaje":f"Bienvenido {usuario}"})

            else:
                
                return render(request,"App/inicio.html",{"mensaje":"Error, datos incorrectos"})

        else:
            
                return render(request,"App/inicio.html" , {"mensaje":"Error, formulario incorrecto"}) 


    form = AuthenticationForm()

    return render(request, "App/login.html", {'form':form})               






def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
       
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"App/inicio.html" , {"mensaje":"Usuario Creado"})

    else:
        form = UserCreationForm()
        form = UserRegisterForm
    return render(request,"App/registro.html" , {"form":form}) 


@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            
            usuario.save()

            return render(request,"App/inicio.html")

    else:
        miFormulario=UserEditForm(initial={'email':usuario.email})


    return render(request,"App/editarPerfil.html", {"miFormulario":miFormulario,"usuario":usuario})    

    
 


class DatosList(LoginRequiredMixin, ListView):
    model = Datos
    template_name = "App/datos_list.html"    



class DatosDetalle(DetailView):
    model = Datos
    template_name = "App/datos_detalle.html"


class DatosCreacion(CreateView):
    model = Datos
    success_url = "/datos/list"
    fields = ['nombre','apellido','edad']



class DatosUpdate(UpdateView):
    model = Datos
    success_url = "/datos/list"
    fields = ['nombre','apellido','edad']



class DatosDelete(DeleteView):
    model = Datos
    success_url = "/datos/list"