from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin 
from apps.registration.models import User,Coordinacion
from apps.reportes.models import Citas
from django.views.generic import View
from django.http import JsonResponse
from django.http import HttpResponseRedirect

# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
            if request.user.email == 'astrofi@inaoep.mx':#if para redirigir a perfil administrador
                return  HttpResponseRedirect(reverse('administradores:reportes_adm'))
            else:#else para redirigir a perfil investigador
                return  HttpResponseRedirect(reverse('reportes:home'))

    else:#else para redirigir a loguearse
        context = {}
        if request.method == "POST":
                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(request, email=email, password=password)
                
                if user:
                   #user.is_authenticated
                   if user.last_login == None:
                       context['sesion'] = "nueva"
                       context['coordinacion'] = Coordinacion.objects.all()
                       
                   login(request,user)
                   
                   if user.is_superuser:
                        return HttpResponseRedirect(reverse('administradores:reportes_adm'))
                   else:
                        if 'sesion' in context:
                            Citas.objects.create(numeral_id = 31,  usuario_id = user.id)
                            return render(request, "core/pantalla_bienvenida.html",context)
                        else:
                            return render(request, "reportes/home.html",context)
                else:
                    context["error"] = '<div class="alert alert-danger col-12" role="alert"><ul><li>Sus credenciales son incorrectas, intentelo de nuevo.<br> Observe que ambos campos pueden ser sensibles a mayúsculas.</li></ul></div>'
                    return render(request,"registration/login.html",context)
        else:
            return render(request,"registration/login.html",context)

class ProfileUpdate(View):
   
    def get(self,request):
        perfil = User.objects.get(id=request.user.id)
        data = {'perfil':perfil}
        return render(request,'registration/perfil.html',data)

    def post(self,request):
        obj = User.objects.get(id=request.user.id)
        nombre = request.POST.get('nombres',obj.nombre)
        apellidos = request.POST.get('apellidos',obj.apellido)
        nombre_corto = request.POST.get('nombre_corto',obj.nombreCorto)
        categoria = request.POST.get('categoria',obj.categoria)
        nivel_sni = request.POST.get('nivel_sni',obj.nivelSni)
        orcid = request.POST.get('orc_id',obj.orcId)
        coordinacion = request.POST.get('coordinacion',obj.coordinacion_id)
        #arxiv_id = request.POST.get('arxiv_id',obj.arxivId)
        
        print(nombre)
        print(apellidos)
        print(nombre_corto)
        print(categoria)
        print(nivel_sni)
        print(orcid)
        print(coordinacion)
        obj.nombre = nombre
        obj.apellido = apellidos
        obj.nombreCorto = nombre_corto
        obj.categoria = categoria
        obj.nivelSni = nivel_sni
        obj.orcId = orcid
        obj.coordinacion_id = int(coordinacion)
        #obj.arxivId = arxiv_id
        obj.save()
        print('pase a guardar todo')

        data= {
            'id':obj.id   
        }
        return JsonResponse(data)