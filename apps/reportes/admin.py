from django.contrib import admin
from .models import  Numeral,Citas,ReporteEnviado,Modelo1,Modelo2,Modelo3,Modelo4,Modelo5,Modelo6,Modelo7,Modelo8,Modelo9,Modelo10,Modelo11,Modelo12,Modelo13,Modelo14,Modelo15,Modelo16,Modelo17,Modelo18,Periodo,Glosario


# Register your models here.
class PersonalizarCampos(admin.ModelAdmin):
    list_display = ('numeral','fecha_de_creacion')

class PersonalizarCitas(admin.ModelAdmin):
    list_display = ('usuario','fecha_de_creacion')

class PersonalizarReportesEnviados(admin.ModelAdmin):
    list_display = ('usuario','reporte','anexo','fecha_de_creacion')

class PersonalizarPeriodo(admin.ModelAdmin):
    list_display = ('nombre_periodo','fecha_inicio')

admin.site.register(Numeral)

admin.site.register(Modelo1,PersonalizarCampos)
admin.site.register(Modelo2,PersonalizarCampos)
admin.site.register(Modelo3,PersonalizarCampos)
admin.site.register(Modelo4,PersonalizarCampos)
admin.site.register(Modelo5,PersonalizarCampos)
admin.site.register(Modelo6,PersonalizarCampos)
admin.site.register(Modelo7,PersonalizarCampos)
admin.site.register(Modelo8,PersonalizarCampos)
admin.site.register(Modelo9,PersonalizarCampos)
admin.site.register(Modelo10,PersonalizarCampos)
admin.site.register(Modelo11,PersonalizarCampos)
admin.site.register(Modelo12,PersonalizarCampos)
admin.site.register(Modelo13,PersonalizarCampos)
admin.site.register(Modelo14,PersonalizarCampos)
admin.site.register(Modelo15,PersonalizarCampos)
admin.site.register(Modelo16,PersonalizarCampos)
admin.site.register(Modelo17,PersonalizarCampos)
admin.site.register(Modelo18,PersonalizarCampos)

admin.site.register(Periodo,PersonalizarPeriodo)

admin.site.register(Citas,PersonalizarCitas)
admin.site.register(ReporteEnviado,PersonalizarReportesEnviados)
admin.site.register(Glosario)