# Redirecciones
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Vistas genericas
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic import View, ListView
import ads
# Librerias para validar el login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Modelos y forms
from .models import  *
from apps.registration.models import User
#from apps.biblioteca.models import Biblioteca
from django.http import JsonResponse

# Manejo Archivos
import os
from django.core.files.base import ContentFile
#Zip
import zipfile
#PDF 
import pdfkit
#config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')  #Linux
config =  pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe') #Windows
# Correo
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from email.mime.base import MIMEBase
from email import encoders
from sistema_reportes.settings import BASE_DIR
#Reporte final
from .generarReporteCoordinacion import generarPdf
#Time zone
import json
from django.contrib import messages
ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7' #Configuramos el token de ADS para las consultas
from datetime import datetime,timedelta

#colocamos un decorador para proteger la vista. #colocamos un decorador para proteger la vista.
@method_decorator(login_required, name='dispatch') 
#heredamos las propiedades de TemplateView de django
class biblioteca_personal(TemplateView): 
    #colocamos el atributo template_name, el cual nos pide la direccion del template a mostrar cuando se ejecute esta clase
    template_name = 'reportes/biblioteca_personal.html' 

#colocamos un decorador para proteger la vista.
@method_decorator(login_required, name='dispatch')
#heredamos las propiedades de TemplateView de django
class busqueda_ads(TemplateView): 
    #colocamos el atributo template_name, el cual nos pide la direccion del template a mostrar cuando se ejecute esta clase
    template_name = 'reportes/busqueda_ads.html'

@method_decorator(login_required, name='dispatch') 
class publicaciones_generales(View):
    def get(self,request):
        # Obtenemos valores de la query a ejecutar junto con su metodo
        query = request.GET.get('query')
        metodo = request.GET.get('metodo')
        articulos = Modelo1.objects.filter(usuario_id=request.user.id) #filtramos los articulos que tenemos ya en la base de datos
        
        #estructuramos condicionales para buscar segun el metodo requerido
        if metodo == 'general':
            data =  list(ads.SearchQuery(q=query,fl='title,pubdate,author,doi,page,volume,pub,bibcode',rows=1000))  # Buscar por autor

        elif metodo == 'bibcode':
            data = list(ads.SearchQuery(bibcode=query,fl='title,pubdate,author,doi,page,volume,pub,bibcode',rows=1000))  # Buscar por bidcode
        
        elif metodo == 'orcid':
            data = list(ads.SearchQuery(orcid=query,fl='title,pubdate,author,doi,page,volume,pub,bibcode',rows=1000))  # Buscar por orcid

        return render(request, 'reportes/publicaciones.html', {'data': data, 'articulos': articulos}) #retornamos un template renderizado junto con un dict para acompletar datos.  

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class agregar_biblioteca(View):
    def post(self,request):
        
        datos = request.POST.getlist('articulos')  
        articulosDB = [] 
        lista = json.loads(datos[0])
        for l in lista:

            fecha_aux = datetime.strptime(l['fecha'], '%Y/%m')
            periodo_mes = fecha_aux.month
            periodo_ano = fecha_aux.year
            
            if periodo_mes < 6:
                periodo_query = Periodo.objects.get(fecha_inicio__year=periodo_ano, fecha_inicio__month=1)
        
            elif periodo_mes >= 6:
                periodo_query = Periodo.objects.get(fecha_inicio__year=periodo_ano, fecha_inicio__month=6)

            obj = Modelo1(
                    autores = l['autores'],
                    titulo = l['titulo'],
                    revista_publicacion = l['pub'],
                    url = 'https://ui.adsabs.harvard.edu/abs/' + l['bibcode'] + '/abstract',
                    doi = l['doi'],
                    fecha = l['fecha'],
                    bibcode = l['bibcode'],
                    paginas = l['page'],
                    volumen = l['volume'],
                    fecha_ano = l['fecha'][0:4],
                    periodo_id = periodo_query.id,
                    usuario_id = request.user.id
                )
            articulosDB.append(obj)
 
        Modelo1.objects.bulk_create(articulosDB)  #creamos todos los objetos de tipo biblioteca en la BD.
        messages.success(request,'<strong>Publicaciones importadas correctamente.<br> Favor de editar la información de sus publicaciones: cuartil, estudiantes, congresos, etc.</strong>')
    
        return JsonResponse({'ok':'ok'})
    
@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class reporte_productividad(View):
    def get(self,request):
        
        periodos = Periodo.objects.all()
        periodoActual =  periodos.last()
        periodos = periodos.order_by("-fecha_inicio")[:2]
        data = {
            'periodoActual': periodoActual,
            'periodos':periodos
        }
        return render(request, 'reportes/reportes_productividad.html',data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class investigacion_cientifica(View):

    def get(self,request):
        id1 = request.GET.get('periodoActual')
        id_usuario = request.user.id  
        periodoActual = Periodo.objects.get(id = id1)
        yearPeriodo = periodoActual.fecha_inicio.year
        data = {
            "numeralName": Numeral.objects.filter(nombre_seccion="Investigacion Cientifica").order_by('orden'),
            'numeral_1': Modelo1.objects.reporteProductividad(id_usuario,1,yearPeriodo),
            'numeral_2': Modelo1.objects.reporteProductividad(id_usuario,2,yearPeriodo), 
            'numeral_3': Modelo1.objects.reporteProductividad(id_usuario,3,yearPeriodo),
            'numeral_4': Modelo1.objects.reporteProductividad(id_usuario,4,yearPeriodo),
            'numeral_5': Modelo1.objects.reporteProductividad(id_usuario,5,yearPeriodo), 
            'numeral_6': Modelo1.objects.reporteProductividad(id_usuario,6,yearPeriodo),
            'numeral_7': Modelo1.objects.reporteProductividad(id_usuario,7,yearPeriodo), 
            'numeral_8': Modelo1.objects.reporteProductividad(id_usuario,8,yearPeriodo),
            'numeral_9': Modelo1.objects.reporteProductividad(id_usuario,9,yearPeriodo),
            "numeral_10": Modelo1.objects.reporteProductividad(id_usuario,10,yearPeriodo),
            'numeral_11': Modelo1.objects.reporteProductividad(id_usuario,11,yearPeriodo), 
            'numeral_12': Modelo1.objects.reporteProductividad(id_usuario,12,yearPeriodo),
            'numeral_13': Modelo1.objects.reporteProductividad(id_usuario,13,yearPeriodo), 
            'numeral_14': Modelo1.objects.reporteProductividad(id_usuario,14,yearPeriodo), 
            'numeral_14a': Modelo1.objects.reporteProductividad(id_usuario,14.1,yearPeriodo),
            'numeral_15':Modelo1.objects.reporteProductividad(id_usuario,15,yearPeriodo),
            'numeral_16':Modelo1.objects.reporteProductividad(id_usuario,16,yearPeriodo),
            'numeral_17':Modelo1.objects.reporteProductividad(id_usuario,17,yearPeriodo),
            'numeral_18':Modelo2.objects.reporteProductividad(id_usuario, 18,yearPeriodo),
            'numeral_19':Modelo2.objects.reporteProductividad(id_usuario, 19,yearPeriodo),
            'numeral_20':Modelo2.objects.reporteProductividad(id_usuario, 20,yearPeriodo),
            'numeral_21':Modelo2.objects.reporteProductividad(id_usuario, 21,yearPeriodo),
            'numeral_22':Modelo2.objects.reporteProductividad(id_usuario, 22,yearPeriodo),
            'numeral_23':Modelo3.objects.reporteProductividad(id_usuario,23,yearPeriodo),
            'numeral_24':Modelo4.objects.reporteProductividad(id_usuario, 24,yearPeriodo),
            'numeral_25':Modelo4.objects.reporteProductividad(id_usuario, 25,yearPeriodo),
            'numeral_26':Modelo4.objects.reporteProductividad(id_usuario, 26,yearPeriodo),
            'numeral_27':Modelo4.objects.reporteProductividad(id_usuario, 27,yearPeriodo),
            'numeral_28':Modelo4.objects.reporteProductividad(id_usuario, 28,yearPeriodo),
            'numeral_29':Modelo4.objects.reporteProductividad(id_usuario, 29,yearPeriodo),
            'citas': Citas.objects.reporteProductividad(id_usuario), #orden - 30
            'glosario': Glosario.objects.reporteProductividad("I. INVESTIGACIÓN CIENTÍFICA"),
        }
        return render(request, "reportes/investigacionCientifica.html", data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class formacion_RH(View):
    
    def get(self,request):
        id1 = request.GET.get('periodoActual')
        id_usuario = request.user.id
        periodoActual = Periodo.objects.get(id = id1)
        yearPeriodo = periodoActual.fecha_inicio.year
        data = {
            'numeralName': Numeral.objects.filter(nombre_seccion="Formacion de Recursos Humanos").order_by('orden'),
            'numeral_31': Modelo5.objects.reporteProductividad(id_usuario,31,yearPeriodo),
            'numeral_32': Modelo5.objects.reporteProductividad(id_usuario,32,yearPeriodo),
            'numeral_33': Modelo5.objects.reporteProductividad(id_usuario,33,yearPeriodo),
            'numeral_34': Modelo5.objects.reporteProductividad(id_usuario,34,yearPeriodo),
            'numeral_35': Modelo6.objects.reporteProductividad(id_usuario,35,yearPeriodo),
            'numeral_36': Modelo6.objects.reporteProductividad(id_usuario,36,yearPeriodo),
            'numeral_37': Modelo7.objects.reporteProductividad(id_usuario,37,yearPeriodo),
            'numeral_38': Modelo13.objects.reporteProductividad(id_usuario,38,yearPeriodo),
            'numeral_39': Modelo7.objects.reporteProductividad(id_usuario,39,yearPeriodo),
            "glosario": Glosario.objects.reporteProductividad("II. FORMACIÓN DE RECURSOS HUMANOS"),
            }
        return render(request, "reportes/formacionRRHH.html", data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class desarrollo_tec_inovacion(View):
    
    def get(self,request):
        id1 = request.GET.get('periodoActual')
        id_usuario = request.user.id
        periodoActual = Periodo.objects.get(id = id1)
        yearPeriodo = periodoActual.fecha_inicio.year
        data = {
            "numeralName": Numeral.objects.filter(nombre_seccion="Desarrollo Tecnologico e Innovacion").order_by('orden'), 
            'numeral_40': Modelo8.objects.reporteProductividad(id_usuario,40,yearPeriodo),
            'numeral_41': Modelo8.objects.reporteProductividad(id_usuario,41,yearPeriodo),
            'numeral_42': Modelo8.objects.reporteProductividad(id_usuario,42,yearPeriodo),
            'numeral_43': Modelo8.objects.reporteProductividad(id_usuario,43,yearPeriodo),
            'numeral_44': Modelo8.objects.reporteProductividad(id_usuario,44,yearPeriodo),
            'numeral_45': Modelo9.objects.reporteProductividad(id_usuario,45,yearPeriodo),
            'numeral_46': Modelo10.objects.reporteProductividad(id_usuario,46,yearPeriodo),
            'glosario':  Glosario.objects.reporteProductividad("III. DESARROLLO TECNOLÓGICO E INNOVACIÓN(agregar patentes en REGISTRO)"),
            }
        return render(request, "reportes/desarrolloTecInnov.html", data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class apoyo_institucional(View):
    
    def get(self,request):
        id1 = request.GET.get('periodoActual')
        id_usuario = request.user.id
        periodoActual = Periodo.objects.get(id = id1)
        yearPeriodo = periodoActual.fecha_inicio.year
        data = {
            "numeralName": Numeral.objects.filter(nombre_seccion="Apoyo Institucional").order_by('orden'),
            'numeral_47': Modelo18.objects.reporteProductividad(id_usuario,47,yearPeriodo),
            'numeral_48': Modelo10.objects.reporteProductividad(id_usuario ,48,yearPeriodo),
            'numeral_49': Modelo11.objects.reporteProductividad(id_usuario,49,yearPeriodo),
            'numeral_49a': Modelo11.objects.reporteProductividad(id_usuario,49.1,yearPeriodo),
            'numeral_49b': Modelo11.objects.reporteProductividad(id_usuario,49.2,yearPeriodo),
            'numeral_50': Modelo11.objects.reporteProductividad(id_usuario,50,yearPeriodo),
            'numeral_51': Modelo11.objects.reporteProductividad(id_usuario,51,yearPeriodo),
            'numeral_52': Modelo11.objects.reporteProductividad(id_usuario,52,yearPeriodo),
            'numeral_52a': Modelo12.objects.reporteProductividad(id_usuario,52.1,yearPeriodo),
            'numeral_53': Modelo13.objects.reporteProductividad(id_usuario,53,yearPeriodo),
            'numeral_54': Modelo13.objects.reporteProductividad(id_usuario,54,yearPeriodo),
            'numeral_55': Modelo14.objects.reporteProductividad(id_usuario,55,yearPeriodo),
            'numeral_56': Modelo14.objects.reporteProductividad(id_usuario,56,yearPeriodo),
            'numeral_57': Modelo18.objects.reporteProductividad(id_usuario,57,yearPeriodo),
            'numeral_58': Modelo15.objects.reporteProductividad(id_usuario,58,yearPeriodo),
            'numeral_59': Modelo16.objects.reporteProductividad(id_usuario,59,yearPeriodo),
            'numeral_60': Modelo18.objects.reporteProductividad(id_usuario,60,yearPeriodo),
            'glosario': Glosario.objects.reporteProductividad("IV. APOYO INSTITUCIONAL"), 
            }
        return render(request, "reportes/apoyoInstitucional.html", data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class informacion_adicional(View):
    def get(self,request):
        id_usuario = request.user.id
        id1 = request.GET.get('periodoActual')
        periodoActual = Periodo.objects.get(id = id1)
        yearPeriodo = periodoActual.fecha_inicio.year

        data = {
            'numeralName': Numeral.objects.filter(nombre_seccion="Informacion Adicional").order_by('orden'),
            'numeral_61': Modelo17.objects.reporteProductividad(id_usuario,61,yearPeriodo),
            'glosario': Glosario.objects.reporteProductividad("V. INFORMACIÖN ADICIONAL"), 
            }

        return render(request, "reportes/informacionAdicional.html", data)

# Investigacion Cientifica - CRUD

# Operaciones Modelo1
@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo1(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo1.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id=numeral_id)
        
        ids = []
        autores = []
        titulo = []
        revista_publicacion = []
        url = []
        doi = []
        fecha = []
        bibcode = []
        paginas = []
        volumen = []
        estudiantes = []
        numeral = []    

        for d in datos:
            numeral_serializer = {}
            data = Modelo1.objects.create(
                autores = d.autores,
                titulo = d.titulo,
                revista_publicacion = d.revista_publicacion,
                url = d.url,
                doi = d.doi,
                fecha = d.fecha,
                bibcode = d.bibcode,
                paginas = d.paginas,
                volumen = d.volumen,
                estudiantes = d.estudiantes,
                
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden
           
            autores.append(data.autores)
            titulo.append(data.titulo)
            revista_publicacion.append(data.revista_publicacion)
            url.append(data.url)
            doi.append(data.doi)
            fecha.append(data.fecha)
            bibcode.append(data.bibcode)
            paginas.append(data.paginas)
            volumen.append(data.volumen)
            estudiantes.append(data.estudiantes) 
            numeral.append(numeral_serializer)
            ids.append(data.id)

        data = {
            'autores':autores,
            'titulo': titulo,
            'revista_publicacion': revista_publicacion,
            'url': url,
            'doi': doi,
            'fecha': fecha,
            'bibcode':bibcode,
            'paginas':paginas,
            'volumen':volumen,    
            'estudiantes': estudiantes,
            'numeral':numeral,
            'ids':ids,
        }
        return  JsonResponse(data)

# Operaciones Modelo2
@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo2(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo2.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id=numeral_id)
        
        nombre_del_proyecto = []
        participantes = []
        estudiantes = []
        rols = []
        descripcion = []
        numeral = []
        ids = []

        for d in datos:
            numeral_serializer = {}
            data = Modelo2.objects.create(
                nombre_del_proyecto = d.nombre_del_proyecto,
                participantes = d.participantes,
                estudiantes = d.estudiantes,
                rol = d.rol,
                descripcion = d.descripcion,
              
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden
            
            nombre_del_proyecto.append(data.nombre_del_proyecto)
            participantes.append(data.participantes)
            estudiantes.append(data.estudiantes)
            rols.append(data.rol)
            descripcion.append(data.descripcion)
            numeral.append(numeral_serializer)
            ids.append(data.id)

        data = {
            'nombre_del_proyecto':nombre_del_proyecto,
            'participantes':participantes,
            'estudiantes':estudiantes,
            'rols':rols,
            'descripcion':descripcion, 
            'numeral':numeral,
            'ids':ids
        }

        return  JsonResponse(data)

# Operaciones Modelo3
@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo3(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        
        datos = Modelo3.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        
        ids = []
        conferencia_proyecto = []
        rol = []
        urls = []
        fecha = []
        numeral = []
                
        for d in datos:
            numeral_serializer = {}
            data = Modelo3.objects.create(
                conferencia_proyecto = d.conferencia_proyecto,
                rol = d.rol,
                url = d.url,
                fecha = d.fecha,

                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden
            
            ids.append(data.id)
            conferencia_proyecto.append(data.conferencia_proyecto)
            rol.append(data.rol)
            urls.append(data.url)
            fecha.append(data.fecha)
            numeral.append(numeral_serializer)        
        
        data = {
            'ids':ids,
            'conferencia_proyecto':conferencia_proyecto,
            'rol':rol,
            'urls':urls,
            'fecha':fecha,   
            'numeral':numeral,
        }
        return  JsonResponse(data)

#Operaciones Modelo4
@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo4(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo4.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        
        ids = []
        titulo = []
        autores = []
        nombre_de_conferencia = []
        fecha = []
        tipo = []
        estudiantes = []
        doi = []
        url = []
        numeral = []
            
        for d in datos:
            numeral_serializer = {}
            data = Modelo4.objects.create(
                titulo = d.titulo,
                autores = d.autores,
                nombre_de_conferencia = d.nombre_de_conferencia,
                fecha = d.fecha,
                tipo = d.tipo,
                estudiantes = d.estudiantes,
                doi = d.doi,
                url = d.url,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden

            ids.append(data.id)
            titulo.append(data.titulo)
            autores.append(data.autores)
            nombre_de_conferencia.append(data.nombre_de_conferencia)
            fecha.append(data.fecha)
            tipo.append(data.tipo)
            estudiantes.append(data.estudiantes)
            doi.append(data.doi)
            url.append(data.url)
            numeral.append(numeral_serializer)
              
        data = {
            'ids':ids,
            'titulo':titulo,
            'autores':autores,
            'nombre_de_conferencia':nombre_de_conferencia,
            'fecha':fecha,
            'tipo':tipo,
            'estudiantes':estudiantes,
            'doi':doi,
            'url':url,
            'numeral':numeral,
        }
        return  JsonResponse(data)

# Formacion RRHH - CRUD
@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo5(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo5.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        
        nombre_completo = []
        titulo_de_tesis = []
        fecha = []
        url = []
        numeral = []
        ids = []

        for d in datos:
            numeral_serializer = {}
            data = Modelo5.objects.create(
                nombre_completo = d.nombre_completo,
                titulo_de_tesis = d.titulo_de_tesis,
                fecha = d.fecha,
                url = d.url,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden
        
            nombre_completo.append(data.nombre_completo)
            titulo_de_tesis.append(data.titulo_de_tesis)
            fecha.append(data.fecha)
            url.append(data.url)
            numeral.append(numeral_serializer)
            ids.append(data.id)

        data = {
            'nombre_completo': nombre_completo,
            'titulo_de_tesis': titulo_de_tesis,
            'fecha': fecha,
            'url': url,
            'numeral':numeral,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo6(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo6.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
  
        nombre_del_curso = []
        periodo_numeral = []
        notas = []
        numeral = []
        ids = []

        for d in datos:
            numeral_serializer = {}
            data = Modelo6.objects.create(
                nombre_del_curso = d.nombre_del_curso,
                periodo_numeral = d.periodo_numeral,
                notas = d.notas,
                
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden
        
            nombre_del_curso.append(data.nombre_del_curso)
            periodo_numeral.append(data.periodo_numeral)
            notas.append(data.notas)
            numeral.append(numeral_serializer)
            ids.append(data.id)

        data = {
            'nombre_del_curso':nombre_del_curso,
            'periodo_numeral':periodo_numeral,
            'notas':notas,
            'numeral':numeral,
            'ids':ids
        }
        print(data)
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo7(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo7.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        
        nombre = []
        titulo_de_tesis = []
        grado = []
        institucion = []
        fecha = []
        notas = []
        numeral = []
        ids = []

        for d in datos:
            numeral_serializer = {}
            data = Modelo7.objects.create(
                nombre = d.nombre,
                titulo_de_tesis = d.titulo_de_tesis,
                grado = d.grado,
                institucion = d.institucion,
                fecha = d.fecha,
                notas = d.notas,

                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden

            nombre.append(data.nombre)
            titulo_de_tesis.append(data.titulo_de_tesis)
            grado.append(data.grado)
            institucion.append(data.institucion)
            fecha.append(data.fecha)
            notas.append(data.notas)
            numeral.append(numeral_serializer)
            ids.append(data.id)

        data = {
            'nombre':nombre,
            'titulo_de_tesis':titulo_de_tesis,
            'grado':grado,
            'institucion':institucion,
            'fecha':fecha,
            'notas':notas,
            'numeral':numeral,
            'ids':ids
        }
        return  JsonResponse(data)

# Desarrollo Tec. Innov. - CRUD
@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo8(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo8.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        
        autores = []
        descripcion = [] 
        url = []
        numeral = []
        ids = []
        
        for d in datos:
            numeral_serializer = {}
            data = Modelo8.objects.create(
                autores = d.autores,
                descripcion = d.descripcion,
                url = d.url,

                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden

            autores.append(data.autores)
            descripcion.append(data.descripcion)
            url.append(data.url)
            numeral.append(numeral_serializer)
            ids.append(data.id)

        data = {
            'autores':autores,
            'descripcion':descripcion,  
            'url':url,
            'numeral':numeral,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo9(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo9.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        
        nombre = []
        descripcion = []
        participantes = []
        financiamiento = []
        numeral = []
        ids = []

        for d in datos:
            numeral_serializer = {}
            data = Modelo9.objects.create(
                nombre = d.nombre,
                descripcion = d.descripcion,
                participantes = d.participantes,
                financiamiento = d.financiamiento,

                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden

            nombre.append(data.nombre)
            descripcion.append(data.descripcion)
            participantes.append(data.participantes)
            financiamiento.append(data.financiamiento)
            numeral.append(numeral_serializer)
            ids.append(data.id)

        data = {
            'nombre':nombre,
            'descripcion':descripcion,
            'participantes':participantes,
            'financiamiento':financiamiento,
            'numeral':numeral,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo10(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        numeral_id = request.GET.get('numeral')
        periodo_id = int(periodo) - 1
        datos = Modelo10.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id = numeral_id)
        
        titulo = []
        autores = []
        numero_reportes = []
        fecha = []
        url = []
        doi = []
        revista_publicacion = []
        numeral = []
        ids = []

        for d in datos:
            numeral_serializer = {}
            data = Modelo10.objects.create(
                titulo = d.titulo,
                autores = d.autores,
                numero_reportes = d.numero_reportes,
                fecha = d.fecha,
                url = d.url,
                doi = d.doi,
                revista_publicacion = d.revista_publicacion,
                
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden

            titulo.append(data.titulo)
            autores.append(data.autores)
            numero_reportes.append(data.numero_reportes)
            fecha.append(data.fecha)
            url.append(data.url)
            doi.append(data.doi)
            revista_publicacion.append(data.revista_publicacion)
            numeral.append(numeral_serializer)
            ids.append(data.id)

        data = {
            'titulo':titulo,
            'autores':autores,
            'numero_reportes':numero_reportes,
            'fecha':fecha,
            'url':url,
            'doi':doi,
            'revista_publicacion':revista_publicacion,
            'numeral':numeral,
            'ids':ids
        }
        return  JsonResponse(data)

# Apoyo institucional
@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo11(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo11.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id = numeral_id)
        
        ids = []
        fecha = []
        descripcion = []
        url = []
        numeral = []
        
             
        for d in datos:
            numeral_serializer = {}
            data = Modelo11.objects.create(
                fecha = d.fecha,
                descripcion = d.descripcion,
                url = d.url,
                
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden

            ids.append(data.id)
            fecha.append(data.fecha)
            descripcion.append(data.descripcion)
            numeral.append(numeral_serializer)
            url.append(data.url)

        data = {
            'ids':ids,
            'fecha':fecha,
            'descripcion':descripcion,
            'numeral':numeral,
            'url':url,      
            
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo12(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo12.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id = numeral_id)
        
        ids =  []
        periodo_numeral = []
        descripcion = []
        numeral = []

        for d in datos:
            numeral_serializer = {}
            data = Modelo12.objects.create(
                periodo_numeral = d.periodo_numeral,
                descripcion = d.descripcion,
                
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden
            
            ids.append(data.id)
            periodo_numeral.append(data.periodo_numeral)
            descripcion.append(data.descripcion)
            numeral.append(numeral_serializer)

        data = {
            'ids':ids,
            'periodo_numeral':periodo_numeral,
            'numeral':numeral,
            'descripcion':descripcion,
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo13(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo13.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id = numeral_id)
        
        ids =  []
        nombre_del_estudiante = []
        descripcion = []  
        fecha = []
        coordinacion = []
        grado = []
        numeral = []
        

        for d in datos:
            numeral_serializer = {}
            data = Modelo13.objects.create(
                nombre_del_estudiante = d.nombre_del_estudiante,
                descripcion = d.descripcion,
                fecha = d.fecha,
                coordinacion = d.coordinacion,
                grado = d.grado,
                
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden

            ids.append(data.id)
            nombre_del_estudiante.append(data.nombre_del_estudiante)
            descripcion.append(data.descripcion)
            fecha.append(data.fecha)
            coordinacion.append(data.coordinacion)
            grado.append(data.grado)
            numeral.append(numeral_serializer)
            
        data = {
            'ids':ids,
            'nombre_del_estudiante':nombre_del_estudiante,
            'descripcion':descripcion,
            'fecha':fecha,
            'coordinacion':coordinacion,
            'grado':grado,
            'numeral':numeral,
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo14(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo14.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id=numeral_id)
        
        ids  = []
        fecha_periodo = []
        descripcion = []
        numeral = []

        for d in datos:
            numeral_serializer = {}
            data = Modelo14.objects.create(
                fecha_periodo = d.fecha_periodo,
                descripcion = d.descripcion,
                
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden

            ids.append(data.id)
            fecha_periodo.append(data.fecha_periodo)
            descripcion.append(data.descripcion)
            numeral.append(numeral_serializer)

        data = {
            'ids':ids,
            'fecha_periodo':fecha_periodo,
            'descripcion':descripcion,
            'numeral':numeral,
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo15(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo15.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id=numeral_id)
        
        laboratorio_taller = []
        numeral = []
        ids  = []

        for d in datos:
            numeral_serializer = {}
            data = Modelo15.objects.create(
                laboratorio_taller = d.laboratorio_taller,
                
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden

            laboratorio_taller.append(data.laboratorio_taller)
            numeral.append(numeral_serializer)
            ids.append(data.id)

        data = {
            'laboratorio_taller':laboratorio_taller,
            'numeral':numeral,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo16(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo16.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id=numeral_id)
        
        ids = []
        descripcion = []
        agencias_financieras = []
        numeral = []
        

        for d in datos:
            numeral_serializer = {}
            data = Modelo16.objects.create(
                descripcion = d.descripcion,
                agencias_financieras = d.agencias_financieras,
                
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden

            descripcion.append(data.descripcion)
            agencias_financieras.append(data.agencias_financieras)
            numeral.append(numeral_serializer)
            ids.append(data.id)

        data = {
            'descripcion':descripcion,
            'agencias':agencias_financieras,
            'numeral':numeral,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo17(View):  
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo17.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        
        ids = []
        telescopio = []
        urls = []
        descripcion = []
        numeral = []

        for d in datos:
            numeral_serializer = {}
            data = Modelo17.objects.create(  
                telescopio_instrumento_infra = d.telescopio_instrumento_infra,
                url = d.url,
                descripcion = d.descripcion,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden

            ids.append(data.id)
            telescopio.append(data.telescopio_instrumento_infra)
            urls.append(data.url)
            descripcion.append(data.descripcion)
            numeral.append(numeral_serializer)
             
        data = {
            'ids':ids,
            'telescopio':telescopio,
            'urls':urls,
            'descripcion':descripcion,
            'numeral':numeral,  
        }
        
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class infoAnteriorModelo18(View):
    def get(self,request):
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo18.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        
        descripcion = []
        numeral = []
        ids = []

        for d in datos:
            numeral_serializer = {}
            data = Modelo18.objects.create(
                descripcion = d.descripcion,
                
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            numeral_serializer['id'] = data.numeral.id
            numeral_serializer['orden'] = data.numeral.orden

            descripcion.append(data.descripcion)
            numeral.append(numeral_serializer)
            ids.append(data.id)
        
        data = {
            'descripcion':descripcion,
            'numeral':numeral,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class enviarReporte(View): 
    def get(self, request):
        #Declaramos variables para filtos y nombres
        
        periodo_id = request.GET.get('periodoActual')
        admin = User.objects.get(is_superuser = 1, coordinacion_id=request.user.coordinacion_id)
        periodo = Periodo.objects.get(id=periodo_id)
        usuario = request.user.id
        yearPeriodo = periodo.fecha_inicio.year
        data = {'periodo':periodo.nombre_periodo,}
        
        if request.user.categoria != 'Sin especificar' and request.user.nivelSni != 'Sin especificar' and request.user.coordinacion and request.user.first_nameCorto:
            data['perfil'] = True
            #Hacemos conexion conn la BD para obtener los anexo de cada nuemral del usuario y del periodo(año)
            anexoModelo1 = Modelo1.objects.anexo(usuario,yearPeriodo)
            anexoModelo2 = Modelo2.objects.anexo(usuario,yearPeriodo)
            anexoModelo3 = Modelo3.objects.anexo(usuario,yearPeriodo)
            anexoModelo4 = Modelo4.objects.anexo(usuario,yearPeriodo)
            anexoModelo5 = Modelo5.objects.anexo(usuario,yearPeriodo)
            anexoModelo6 = Modelo6.objects.anexo(usuario,yearPeriodo)
            anexoModelo7 = Modelo7.objects.anexo(usuario,yearPeriodo)
            anexoModelo8 = Modelo8.objects.anexo(usuario,yearPeriodo)
            anexoModelo9 = Modelo9.objects.anexo(usuario,yearPeriodo)
            anexoModelo10 = Modelo10.objects.anexo(usuario,yearPeriodo)
            anexoModelo11 = Modelo11.objects.anexo(usuario,yearPeriodo)
            anexoModelo12 = Modelo12.objects.anexo(usuario,yearPeriodo)
            anexoModelo13 = Modelo13.objects.anexo(usuario,yearPeriodo)
            anexoModelo14 = Modelo14.objects.anexo(usuario,yearPeriodo)
            anexoModelo15 = Modelo15.objects.anexo(usuario,yearPeriodo)
            anexoModelo16 = Modelo16.objects.anexo(usuario,yearPeriodo)
            anexoModelo17 = Modelo17.objects.anexo(usuario,yearPeriodo)
            anexoModelo18 = Modelo18.objects.anexo(usuario,yearPeriodo)
            anexoCitas = Citas.objects.anexo(usuario)

            #Mandamos a llamar a la funcion que genera el PDF.
            html = generarPdf(request,periodo_id)
            
            options = {
                'page-size': 'Letter',
                'margin-top': '0.75in',
                'margin-right': '0.75in',
                'margin-bottom': '0.75in',
                'margin-left': '0.75in',
                'encoding': "UTF-8",
                'no-outline': None
            }
            pdf = pdfkit.from_string(html,False,configuration=config,options=options)        
            
            #Email para investigador
            """
            body = render_to_string(
                'reportes/templateReportesFinalizadoUsuario.html', {
                    'nombre': request.user.first_name,
                    'apellido': request.user.apellido,
                    'periodo':periodo.nombre_periodo,
                },
            )
            
            email_message = EmailMessage(
                subject='Reporte enviado a la Coordinación',
                body=body,
                from_email='reportes-astro@inaoep.mx',
                to=[request.user.email],
            )

            email_message.content_subtype = 'html'
            #Convertimos la instancia PDF en un tipo MIME para enviarlo
            adjunto = MIMEBase('application', 'application/pdf')
            adjunto.set_payload(pdf)
            encoders.encode_base64(adjunto)
            adjunto.add_header('Content-Disposition', "attachment; filename= Reporte "+periodo.nombre_periodo+'.pdf')
            email_message.attach(adjunto)
            #Enviamos email
            email_message.send()
            
            #Email para la coordinacionP
            bodyAdmin = render_to_string(
            'reportes/templateReporteFinalizado.html',{
                'nombre':request.user.first_name,
                'apellido': request.user.apellido,
                'periodo': periodo.nombre_periodo,
            }   
            )
            """
            """
            if admin.correoAlternativo:
                mensajeCordinacion = EmailMessage(
                    subject='Reporte enviado a la Coordinación',
                    body=bodyAdmin,
                    from_email='reportes-astro@inaoep.mx',
                    to=['reportes-astro@inaoep.mx',admin.email,admin.correoAlternativo],
                )
            else:
                mensajeCordinacion = EmailMessage(
                    subject='Reporte enviado a la Coordinación',
                    body=bodyAdmin,
                    from_email='reportes-astro@inaoep.mx',
                    to=['reportes-astro@inaoep.mx',admin.email],
                )

            mensajeCordinacion.content_subtype = 'html'
            mensajeCordinacion.attach(adjunto)
            #Enviamos email
            mensajeCordinacion.send()
            """
            #creamos o actualizamos reporte en BD
            obj,creado = ReporteEnviado.objects.get_or_create(periodo_id = periodo_id, usuario_id = request.user.id)
            
            if creado:
                data['actualizado'] = False

            else:
                data['actualizado'] = True
                if obj.reporte:
                    os.remove(os.path.join(BASE_DIR + '/media/'+obj.reporte.name))
                if obj.anexo:
                    os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexo.name))
                
            obj.reporte.save('Reporte '+periodo.nombre_periodo+' '+str(request.user.first_name)+'.pdf', ContentFile(pdf), save=False)
            print(BASE_DIR+ '/media/'+'anexo_zip/anexo.zip')
            print(os.path.isdir(os.path.dirname(BASE_DIR+ '/media/'+'anexos_zip/anexo.zip')))
            
            #Genera Zip con anexo
            with zipfile.ZipFile(BASE_DIR + '/media/'+'anexos_zip/anexo.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as anexoZip:
                
                for anexo in anexoModelo1:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)
                
                for anexo in anexoModelo2:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)            
                
                for anexo in anexoModelo3:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)            
                
                for anexo in anexoModelo4:        
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)            
                
                for anexo in anexoModelo5:        
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)            
                
                for anexo in anexoModelo6:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)            
            
                for anexo in anexoModelo7:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)            
                
                for anexo in anexoModelo8:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)            
                
                for anexo in anexoModelo9:   
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)            
                
                for anexo in anexoModelo10:    
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)            
                
                for anexo in anexoModelo11:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)            
                
                for anexo in anexoModelo12:        
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)            
                
                for anexo in anexoModelo13:        
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)            
                
                for anexo in anexoModelo14:        
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)            
                
                for anexo in anexoModelo15:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)
                
                for anexo in anexoModelo16:        
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)
                
                for anexo in anexoModelo17:        
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)

                for anexo in anexoModelo18:        
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)
                
                for anexo in anexoCitas:        
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexo.name, anexo.anexo.name)
            
            anexoZip.close()

            anexoZip = open(BASE_DIR + '/media/'+'anexos_zip/anexo.zip','rb') #Corregir este error
            obj.anexo.save("Anexo "+periodo.nombre_periodo+' '+str(request.user.first_name)+".zip", ContentFile(anexoZip.read()), save=False)
            obj.save()
            
        else:
            data['perfil'] = False
        
        return  JsonResponse(data)

# Generar PDF
@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class generarReporte(View):
    def post(self,request):
        periodo_id = request.POST.get('periodo')
        html = generarPdf(request,periodo_id)
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None
        }
        pdf  = pdfkit.from_string(html,False,configuration=config,options=options)
        return HttpResponse(pdf,content_type='application/pdf')
           
@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class reportesEnviados(View):
    def get(self,request):
        queryset = ReporteEnviado.objects.filter(usuario_id= request.user.id)
        return render(request,'reportes/historico.html')

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class home(TemplateView):
    template_name = 'reportes/home.html'

@method_decorator(login_required, name='dispatch') #colocamos un decorador para proteger la vista.
class ampliarSesion(View):
    def get(self, request):
        request.session.set_expiry(600)
        request.session.get_expiry_date()

        timeNow = datetime.now() + timedelta(minutes=10)
        hora = timeNow.hour
        minutos = timeNow.minute
        nuevaSesion = str(hora) + ":" + str(minutos)
    
        data = { 'nuevaSesion': nuevaSesion }
        return JsonResponse(data)