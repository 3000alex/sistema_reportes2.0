from django.db import models
from apps.registration.models import User
from datetime import *
from .managers import (modelo1Manager,modelo2Manager,modelo3Manager,modelo4Manager,modelo5Manager,modelo6Manager,modelo7Manager,modelo8Manager,modelo9Manager,modelo10Manager
,modelo11Manager,modelo12Manager,modelo13Manager,modelo14Manager,modelo15Manager,modelo16Manager,modelo17Manager, modelo18Manager, citasManager,glosarioManager)
# Create your models here.
Seccionselect = (
        ('Investigacion Cientifica','Investigacion Cientifica'),
        ('Formacion de Recursos Humanos','Formacion de Recursos Humanos'),
        ('Desarrollo Tecnologico e Innovacion','Desarrollo Tecnologico e Innovacion'),
        ('Apoyo Institucional','Apoyo Institucional'),
        ('Informacion Adicional','Informacion Adicional'),
    )

TelescopioChoise = (
    ('Telescopio','Telescopio'),
    ('Instrumento','Instrumento'),
    ('Infraestructura','Infraestructura')
)

Presentacionselect = (
    ('Presentación Oral','Presentación Oral'),
    ('Poster','Poster'),
)

gradoselect = (
    ('Licenciatura','licenciatura'),
    ('Maestría','maestría'),
    ('Doctorado','doctorado'),
)

ResponsableSelect = (
    ('Responsable técnico','Responsable técnico'),
    ('Participante','Participante'),
)

GlosarioSelect = (
    ('I. INVESTIGACIÓN CIENTÍFICA', 'I. INVESTIGACIÓN CIENTÍFICA'),
    ('II. FORMACIÓN DE RECURSOS HUMANOS', 'II. FORMACIÓN DE RECURSOS HUMANOS'),
    ('III. DESARROLLO TECNOLÓGICO E INNOVACIÓN(agregar patentes en REGISTRO)', 'III. DESARROLLO TECNOLÓGICO E INNOVACIÓN(agregar patentes en REGISTRO)'),
    ('IV. APOYO INSTITUCIONAL', 'IV. APOYO INSTITUCIONAL'),
    ('V. INFORMACIÖN ADICIONAL', 'V. INFORMACIÖN ADICIONAL' ),
)

class Numeral(models.Model):
    nombre = models.CharField(max_length=190,verbose_name="Nombre del numeral",blank=True)
    nombre_seccion = models.CharField(max_length=150,verbose_name="Nombre de la seccion",choices=Seccionselect)
    orden = models.FloatField(verbose_name="Orden",)

    class Meta:
        verbose_name="Numeral"
        verbose_name_plural = "Numerales"
        ordering = ['orden']
    
    def __str__(self):
        return self.nombre

class Periodo(models.Model):
    nombre_periodo = models.CharField(max_length=150, verbose_name="Nombre del periodo")
    fecha_inicio = models.DateTimeField(verbose_name="Fecha del inicio de periodo",auto_now_add=True)
    
    class Meta:
        verbose_name="Periodo del reporte"
        verbose_name_plural = "Periodos de los reportes"
        ordering = ['fecha_inicio']
    
    def __str__(self):
        return self.nombre_periodo

class Glosario(models.Model):
    seccion = models.CharField(max_length=200, verbose_name="Seccion perteneciente", choices=GlosarioSelect)
    numerales = models.TextField(max_length=5000, verbose_name="Nombre del numeral")
    explicacion = models.TextField(max_length=5000, verbose_name="Explicación")
    
    objects = glosarioManager()

    class Meta:
        verbose_name = "glosario"
        verbose_name_plural = "Glosarios"
        ordering = ['numerales']
    
    def __str__(self):
        return self.seccion

#Modelo 1 comprende los numerales 6,8,10,15,16,17,
#  15-17(A excepcion del campo estudiantes)
class Modelo1(models.Model):
    usuario =  models.ForeignKey(User,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE, null=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, null=True)
    
    autores = models.TextField(max_length=15000,verbose_name="Nombre de los autores", blank=True)
    titulo = models.TextField(max_length=15000,verbose_name="Nombre del titulo", blank=True)
    revista_publicacion = models.CharField(max_length=250,verbose_name="Nombre de la revista o publicacion", blank=True)
    url = models.CharField(max_length=100,verbose_name="url del articulo", blank=True)
    doi = models.CharField(max_length=150,verbose_name="Nombre de doi", blank=True)
    fecha = models.CharField(max_length=100, verbose_name="Fecha del articulo", blank=True)
    bibcode = models.CharField(max_length=80, verbose_name="bibcode",blank=True,default='')
    paginas = models.CharField(max_length=150, blank=True,default='')
    volumen = models.CharField(max_length=150, blank=True,default='')
    estudiantes = models.CharField(max_length=250,verbose_name="Nombre de los estudiantes en el articulo", blank=True)
    fecha_ano = models.CharField(max_length=50,verbose_name="Fecha", blank=True,default='')
    anexo = models.FileField(verbose_name="archivo PDF",  upload_to='anexos/',blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo1Manager()

    class Meta:
        verbose_name="Campo Modelo 1"
        verbose_name_plural = "Campos del Modelo 1"
        ordering = ['autores']

    def __str__(self):
        return self.numeral.nombre

#Modelo 2 comprende los numerales 18-22
class Modelo2(models.Model):
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    nombre_del_proyecto = models.CharField(max_length=500,verbose_name="Nombre del proyecto",blank=True)
    participantes = models.TextField(max_length=500,verbose_name="participantes",blank=True)
    estudiantes = models.CharField(max_length=10000,verbose_name="estudiantes",blank=True)
    rol = models.CharField(max_length=500,verbose_name="Rol", blank=True,choices=ResponsableSelect)
    descripcion = models.TextField(max_length=15000,verbose_name="descripcion",blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects = modelo2Manager()

    class Meta:
        verbose_name="campo Modelo 2"
        verbose_name_plural = "Campos del Modelo 2"
        ordering = ['nombre_del_proyecto']

    def __str__(self):
        return self.numeral.nombre

#Modelo 3 Comprende el numeral 23{Conferencia,rol,url,fecha}
class Modelo3(models.Model):
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    conferencia_proyecto = models.CharField(max_length=500,  verbose_name="Conferencia o proyecto", blank=True)
    rol = models.CharField(max_length=500,  verbose_name="rol", blank=True)
    url = models.CharField(max_length=100,verbose_name="url", blank=True) 
    fecha = models.CharField(max_length=200,  verbose_name="fecha", blank=True)
    anexo = models.FileField(verbose_name="anexo", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo3Manager()

    class Meta:
        verbose_name="campo Modelo 3"
        verbose_name_plural = "Campos del Modelo 3"
        ordering = ['conferencia_proyecto']

    def __str__(self):
        return self.numeral.nombre

#Modelo 4(antes 3) comprende los numerales 24-25, 26-27(Sin el campo presentacion Oral o Poster), 28-29(default)
class Modelo4(models.Model):
    usuario =  models.ForeignKey(User,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    titulo = models.CharField(max_length=500,verbose_name="Titulo de la presentacion", blank=True)
    autores = models.TextField(max_length=15000,verbose_name="Nombre de los autores", blank=True)
    nombre_de_conferencia = models.CharField(max_length=500,verbose_name="Nombre de la conferencia", blank=True)
    fecha = models.CharField(max_length=500,verbose_name="fecha", blank=True)
    tipo = models.CharField(max_length=500,verbose_name="Presentacion oral o poster",choices=Presentacionselect, blank=True)
    estudiantes = models.CharField(max_length=10000,verbose_name="Nombre de los estudiantes", blank=True)
    doi = models.CharField(max_length=500,verbose_name="DOI/ISBN", blank=True)
    url = models.CharField(max_length=500,verbose_name="Nombre de la url", blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/',blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects = modelo4Manager()

    class Meta:
        verbose_name="campo Modelo 4"
        verbose_name_plural = "Campos del Modelo 4"
        ordering = ['titulo']

    def __str__(self):
        return self.numeral.nombre

#Modelo 5(antes 4) comprende los numerales 31-34
class Modelo5(models.Model):
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    nombre_completo = models.CharField(max_length=500,verbose_name="Nombre completo", blank=True)
    titulo_de_tesis = models.CharField(max_length=500,verbose_name="Titulo de tesis", blank=True)
    fecha = models.CharField(max_length=500,verbose_name="fecha", blank=True)
    url = models.CharField(max_length=500,verbose_name="link de la url", blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo5Manager()

    class Meta:
        verbose_name="campo Modelo 5"
        verbose_name_plural = "Campos del Modelo 5"
        ordering = ['nombre_completo']

    def __str__(self):
        return self.numeral.nombre

#Modelo 6 (antes 5) comprende los numerales 35-36
class Modelo6(models.Model):
    usuario =  models.ForeignKey(User,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    nombre_del_curso = models.CharField(max_length=500,verbose_name="Nombre del Curso", blank=True)
    periodo_numeral = models.CharField(max_length=500,verbose_name="Periodo del numeral", blank=True)
    notas = models.CharField(max_length=500,verbose_name="Notas", blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo6Manager()

    class Meta:
        verbose_name="campo Modelo 6"
        verbose_name_plural = "Campos del Modelo 6"
        ordering = ['nombre_del_curso']

    def __str__(self):
        return self.numeral.nombre

#Modelo 7(antes 6) comprende a los numerales 37(Sin el atributo de fecha),39
class Modelo7(models.Model):
    usuario =  models.ForeignKey(User,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    nombre = models.CharField(max_length=500,verbose_name="Nombre", blank=True)
    titulo_de_tesis = models.CharField(max_length=500,verbose_name="titulo de la tesis", blank=True)
    grado = models.CharField(max_length=500,verbose_name="Tipo de grado", blank=True,choices=gradoselect)
    institucion = models.CharField(max_length=500,verbose_name="Institucion", blank=True)
    fecha = models.CharField(max_length=500,verbose_name="fecha", blank=True)
    notas = models.CharField(max_length=500,verbose_name="notas", blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo7Manager()

    class Meta:
        verbose_name="campo Modelo 7"
        verbose_name_plural = "Campos del Modelo 7"
        ordering = ['nombre']

    def __str__(self):
        return self.numeral.nombre

#Modelo 8(antes 7) comprende numerales 40-44
class Modelo8(models.Model):
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    autores = models.TextField(max_length=15000,verbose_name="autores", blank=True)
    descripcion = models.TextField(max_length=15000,verbose_name="descripcion", blank=True)
    url = models.CharField(max_length=500,verbose_name="url", blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo8Manager()

    class Meta:
        verbose_name="campo Modelo 8"
        verbose_name_plural = "Campos del Modelo 8"
        ordering = ['autores']

    def __str__(self):
        return self.numeral.nombre

#Modelo 9(antes 8) comprende numeral 45
class Modelo9(models.Model):
    usuario =  models.ForeignKey(User,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    nombre = models.CharField(max_length=500,verbose_name="nombre", blank=True)
    descripcion = models.TextField(max_length=15000,verbose_name="descripcion", blank=True)
    participantes = models.TextField(max_length=500,verbose_name="participantes", blank=True)
    financiamiento = models.CharField(max_length=500,verbose_name="financiamiento", blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo9Manager()

    class Meta:
        verbose_name="campo Modelo 9"
        verbose_name_plural = "Campos del Modelo 9"
        ordering = ['nombre']

    def __str__(self):
        return self.numeral.nombre

#Modelo10 (antes 9) comprende los numerales 46 (Sin revista o publcacion ni doi) 
# y el 48
class Modelo10(models.Model):
    usuario =  models.ForeignKey(User,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    titulo = models.TextField(max_length=15000,verbose_name="titulo", blank=True)
    autores = models.TextField(max_length=15000,verbose_name="autores", blank=True)
    numero_reportes = models.CharField(max_length=500,verbose_name="numero de reportes", blank=True)
    fecha = models.CharField(max_length=500,verbose_name="fecha", blank=True)
    url = models.CharField(max_length=500,verbose_name="url", blank=True)
    doi = models.CharField(max_length=500,verbose_name="doi", blank=True)
    revista_publicacion = models.CharField(max_length=500,verbose_name="revista o publicacion", blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo10Manager()

    class Meta:
        verbose_name="campo Modelo 10"
        verbose_name_plural = "Campos del Modelo 10"
        ordering = ['titulo']

    def __str__(self):
        return self.numeral.nombre

#El modelo 11 (antes 10) 
# numeral 49 - 52 
class Modelo11(models.Model):
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    fecha = models.CharField(max_length=500,verbose_name="fecha", blank=True)
    descripcion = models.TextField(max_length=15000,verbose_name="descripcion", blank=True)
    url = models.CharField(max_length=500,verbose_name="url", blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/',blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo11Manager()

    class Meta:
        verbose_name="campo Modelo 11"
        verbose_name_plural = "Campos del Modelo 11"
        ordering = ['fecha']

    def __str__(self):
        return self.numeral.nombre

# modelo12 52a(Con sus campos Descripcion y periodo)
class Modelo12(models.Model):
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    periodo_numeral = models.CharField(max_length=500,verbose_name="periodo", blank=True)
    descripcion = models.TextField(max_length=15000,verbose_name="descripcion", blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/',blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo12Manager()

    class Meta:
        verbose_name="campo Modelo 12"
        verbose_name_plural = "Campos del Modelo 12"
        ordering = ['periodo_numeral']

    def __str__(self):
        return self.numeral.nombre

#El modelo 13(antes 11) comprende los numerales 53(Sin el atributo fecha), 54 
#Se incluyo lo que era modelo16 referente al numeral 38
class Modelo13(models.Model):
    usuario =  models.ForeignKey(User,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    nombre_del_estudiante = models.CharField(max_length=500,verbose_name="Nombre del estudiante", blank=True)
    descripcion = models.TextField(max_length=15000,verbose_name="Descripcion", blank=True)
    fecha = models.CharField(max_length=500,verbose_name="Fecha", blank=True)
    coordinacion = models.CharField(max_length=500,  verbose_name="Coordinacion", blank=True)
    grado = models.CharField(max_length=500,  verbose_name="grado", blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo13Manager()

    class Meta:
        verbose_name="campo Modelo 13"
        verbose_name_plural = "Campos del Modelo 13"
        ordering = ['nombre_del_estudiante']

    def __str__(self):
        return self.numeral.nombre

#modelo 14 55-56 (Fecha o periodo)
class Modelo14(models.Model):
    usuario =  models.ForeignKey(User,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    fecha_periodo = models.CharField(max_length=500,verbose_name="Fecha", blank=True)
    descripcion = models.TextField(max_length=15000,verbose_name="Descripcion", blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo14Manager()

    class Meta:
        verbose_name="campo Modelo 14"
        verbose_name_plural = "Campos del Modelo 14"
        ordering = ['fecha_periodo']

    def __str__(self):
        return self.numeral.nombre

#Modelo modelo15 (antes 12) comprende el numeral 58
class Modelo15(models.Model):
    usuario =  models.ForeignKey(User,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    laboratorio_taller = models.CharField(max_length=500,verbose_name="Laboratorio o taller", blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo15Manager()

    class Meta:
        verbose_name="campo Modelo 15"
        verbose_name_plural = "Campos del Modelo 15"
        ordering = ['laboratorio_taller']

    def __str__(self):
        return self.numeral.nombre

#Modelo 16 (antes 13) comprende el numeral 59
class Modelo16(models.Model):
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    descripcion = models.TextField(max_length=15000,verbose_name="Descripcion", blank=True)
    agencias_financieras = models.CharField(max_length=500,verbose_name="Agencias Financieras", blank=True)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo16Manager()

    class Meta:
        verbose_name="campo Modelo 16"
        verbose_name_plural = "Campos del Modelo 16"
        ordering = ['descripcion']

    def __str__(self):
        return self.numeral.nombre

#Modelo 17 (antes 14) Comprende el numeral 61
class Modelo17(models.Model):
    usuario =  models.ForeignKey(User, on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    telescopio_instrumento_infra = models.CharField(max_length=500,verbose_name="Telescopio, instrumento, infraestructura", blank=True)
    url = models.CharField(max_length=100,verbose_name="url", blank=True)
    descripcion = models.TextField(max_length=15000, verbose_name="Descripcion", blank=True)
    anexo = models.FileField(verbose_name="anexo", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo17Manager()

    class Meta:
        verbose_name="campo Modelo 17"
        verbose_name_plural = "Campos del Modelo 17"
        ordering = ['telescopio_instrumento_infra']

    def __str__(self):
        return self.numeral.nombre

# Modelo 18 (antes 15) comprende los nuumerales 47,57,60 
class Modelo18(models.Model):
    usuario =  models.ForeignKey(User,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    
    descripcion = models.TextField(max_length=15000,verbose_name="descripcion", blank=True)
    anexo = models.FileField(verbose_name="anexo", upload_to='anexos/', blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects  = modelo18Manager()

    class Meta:
        verbose_name="campo Modelo 18"
        verbose_name_plural = "Campos del Modelo 18"
        ordering = ['descripcion']

    def __str__(self):
        return self.numeral.nombre

class Citas(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    
    citas = models.IntegerField(verbose_name="Citas", default=0)
    citas_en_periodo = models.IntegerField(verbose_name="Citas durante periodo del reporte", default=0)
    indiceH = models.IntegerField(verbose_name="Indice H",  default=0)
    anexo = models.FileField(verbose_name="archivo PDF", upload_to='anexos/',blank=True)
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    objects = citasManager()

    class Meta:
        verbose_name ="cita del periodo"
        verbose_name_plural = "Citas del periodo"
        ordering = ['usuario']

    def __str__(self):
        return self.numeral.nombre

class ReporteEnviado(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE, verbose_name="periodo")
    reporte = models.FileField(verbose_name="reporte", blank=True, upload_to='reportes/pdfs/')
    anexo = models.FileField(verbose_name="anexos", blank=True, upload_to='reportes/anexos/')
    fecha_de_creacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha")

    class Meta:
        verbose_name = "Reporte Enviado"
        verbose_name_plural = "Reportes Enviados"
        ordering = ['usuario']

    def __str__(self):
        return self.periodo.nombre_periodo