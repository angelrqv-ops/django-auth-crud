from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from .clasesGenerales import clasesGenerales
from .models import Services
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home.html')

def singup(request):
    if request.method == "GET":
        mensaje = ''
        return render(request, 'singup.html', {
            'formDjango': UserCreationForm,
            'messajeError': mensaje
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                tipoUsuario = int(request.POST['tipouser'])
                ultimoUsuario = User.objects.last()
                clasesGenerales.createTipodeUsuario(ultimoUsuario, tipoUsuario)
                # si se crea el usuario redirecciona al login
                mensaje = 'Ahora puedes iniciar sesión'
                return render(request, 'login.html', {
                    'loginDjango': AuthenticationForm,
                    'mensaje': mensaje
                })
            except Exception as e:
                # si tiene algun tipo de error lo manda al singup
                print(e)
                mensaje = clasesGenerales.errorMessages(str(e))
                return render(request, 'singup.html', {
                    'formDjango': UserCreationForm,
                    'messajeError': mensaje
                })
        else:
            # si las contraseñas no coinciden carga el formulario y manda el mensaje
            mensaje = 'Las contraseñas no coinciden'
            return render(request, 'singup.html', {
                'formDjango': UserCreationForm,
                'messajeError': mensaje
            })

def logueo(request):
    mensaje = ''
    if request.method == 'GET':
        return render(request, 'login.html', {
            'loginDjango': AuthenticationForm,
            'mensaje': mensaje
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            mensaje = 'Usuario o contraseña incorrecto'
            return render(request, 'login.html', {
                'loginDjango': AuthenticationForm,
                'mensaje': mensaje
            })
        else:
            print(user)
            login(request, user)
            return redirect('/crudService/')
@login_required
def crudServices(request):
    services = Services.objects.all()
    if request.method == 'GET':
        return render(request, 'crudservices.html', {
            'services': services
        })
    else:
        serviceName = request.POST['nombreservicio']
        services = clasesGenerales.createServicio(serviceName)
        return redirect('/crudService/')
@login_required
def deslogueo(request):
    logout(request)
    return redirect('login')
@login_required
def updateservice(request):
    if request.method == 'POST':
        idService = request.POST['serviceId']
        serviceName = request.POST['nombreservicioModal']
        service =  clasesGenerales.updateServicio(idService, serviceName)
        return redirect('/crudService/')
    else:
        return redirect('/crudService/')   
@login_required
def deleteservice(request):
    if request.method == 'POST':
        idService = request.POST['serviceIddelete']
        print(idService)
        clasesGenerales.deleteServicio(idService)
        return redirect('/crudService/')
    else:
        return redirect('/crudService/') 