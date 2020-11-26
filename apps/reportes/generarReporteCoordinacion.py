from .models import Numeral, Citas, Modelo1, Modelo2, Modelo3, Modelo4, Modelo5, Modelo6, Modelo7, Modelo8, Modelo9, Modelo10
from .models import Modelo11, Modelo12, Modelo13, Modelo14, Modelo15, Modelo16,Modelo17,Modelo18, Periodo
from apps.registration.models import User
#from apps.biblioteca.models import Biblioteca
from datetime import date
from datetime import datetime
from django.http import HttpResponse
from django.template.loader import get_template

def generarPdf(request,periodo_id):
    template = get_template('reportes/templateReporte.html')
    #periodo = Periodo.objects.last()
    periodo = Periodo.objects.get(id=periodo_id) #Para obtener valores del 2019
    yearPeriodo = periodo.fecha_inicio.year
    usuario_id = request.user.id
    
    mesFin = ""
    if periodo.fecha_inicio.month == 1:
        mesFin = "JUNIO"
    elif periodo.fecha_inicio.month == 6:
        mesFin = "DICIEMBRE"
    
    dataReporte = {
        'fecha_inicioP': periodo.fecha_inicio,
        'mesFin':mesFin,
        'datosInvestigador': User.objects.get(id=usuario_id),
        'numeral': Numeral.objects.all(),
        'coordinacion':request.user.coordinacion,
        'citas': Citas.objects.generarPdf(usuario_id),
        #'biblioteca': Biblioteca.objects.generarPdf(usuario_id,yearPeriodo),
        
        'modelo1': Modelo1.objects.generarPdf(usuario_id,yearPeriodo),
        'modelo2': Modelo2.objects.generarPdf(usuario_id,yearPeriodo),
        'modelo3': Modelo3.objects.generarPdf(usuario_id,yearPeriodo),
            
        #Formacion_RH
        'modelo4': Modelo4.objects.generarPdf(usuario_id,yearPeriodo),
        'modelo5': Modelo5.objects.generarPdf(usuario_id,yearPeriodo),
        'modelo6': Modelo6.objects.generarPdf(usuario_id,yearPeriodo),
        #Desarrollo Tec. Inn.
        'modelo7': Modelo7.objects.generarPdf(usuario_id,yearPeriodo),
        'modelo8': Modelo8.objects.generarPdf(usuario_id,yearPeriodo),
        'modelo9': Modelo9.objects.generarPdf(usuario_id,yearPeriodo),
            
        #Apoyo Institucional
        'modelo10': Modelo10.objects.generarPdf(usuario_id,yearPeriodo),
        'modelo11': Modelo11.objects.generarPdf(usuario_id,yearPeriodo),
        'modelo12': Modelo12.objects.generarPdf(usuario_id,yearPeriodo),
        'modelo13': Modelo13.objects.generarPdf(usuario_id,yearPeriodo),
        #Informacion Adicional
        'modelo14': Modelo14.objects.generarPdf(usuario_id,yearPeriodo),
        'modelo15': Modelo15.objects.generarPdf(usuario_id,yearPeriodo),
        
        'modelo16': Modelo16.objects.generarPdf(usuario_id,yearPeriodo),
        'modelo17': Modelo17.objects.generarPdf(usuario_id,yearPeriodo),
        'modelo18': Modelo18.objects.generarPdf(usuario_id,yearPeriodo),
    }
    html = template.render(dataReporte)

    return html