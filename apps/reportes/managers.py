from django.db import models
from django.db.models import Q

class modelo1Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def biblioteca_astrofisica(self, user_id):
        response = self.filter(
            Q(usuario_id=user_id, numeral = 1) | 
            Q(usuario_id=user_id, numeral = 2) | 
            Q(usuario_id=user_id, numeral = 3) | 
            Q(usuario_id=user_id, numeral = 4) | 
            Q(usuario_id=user_id, numeral = 5) | 
            Q(usuario_id=user_id, numeral = 7) | 
            Q(usuario_id=user_id, numeral = 9) | 
            Q(usuario_id=user_id, numeral = 11) | 
            Q(usuario_id=user_id, numeral = 12) | 
            Q(usuario_id=user_id, numeral = 13) |
            Q(usuario_id=user_id, numeral = 14) |
            Q(usuario_id=user_id, numeral = 15) |
            Q(usuario_id=user_id, numeral = None)

            )
        return response

    def reporteProductividad_sinOrden(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response
    
    def entradasContador(self,year,orden,distinct,request):
        response = self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).order_by(distinct).distinct(distinct)
        response = str(response.count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo2Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response

    def entradasContador(self,year,orden,distinct,request):
        response = self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).order_by(distinct).distinct(distinct)
        response = str(response.count())
        return response

    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo3Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response
    
    def entradasContador(self,year,orden,distinct,request):
        response = self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).order_by(distinct).distinct(distinct)
        response = str(response.count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo4Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response

    def entradasContador(self,year,orden,distinct,request):
        response = self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).order_by(distinct).distinct(distinct)
        response = str(response.count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo5Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response
    
    def entradasContador(self,year,orden,distinct,request):
        response = self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).order_by(distinct).distinct(distinct)
        response = str(response.count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo6Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response
    
    def entradasContador(self,year,orden,distinct,request):
        response = self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).order_by(distinct).distinct(distinct)
        response = str(response.count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo7Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response

    def entradasContador(self,year,orden,distinct,request):
        response = self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).order_by(distinct).distinct(distinct)
        response = str(response.count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo8Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response
    
    def entradasContador(self,year,orden,distinct,request):
        response = self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).order_by(distinct).distinct(distinct)
        response = str(response.count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo9Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response

    def entradasContador(self,year,orden,distinct,request):
        response = self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).order_by(distinct).distinct(distinct)
        response = str(response.count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo10Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response

    def entradasContador(self,year,orden,distinct,request):
        response = self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).order_by(distinct).distinct(distinct)
        response = str(response.count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo11Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response
    
    def entradasContador(self,year,orden,request):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo12Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response
    
    def entradasContador(self,year,orden,request):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo13Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response
    
    def entradasContador(self,year,orden,request):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo14Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response
    
    def entradasContador(self,year,orden,request):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo15Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response

    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response
    
    def entradasContador(self,year,orden,request):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo16Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response

    def entradasContador(self,year,orden,request):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo17Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response

    def entradasContador(self,year,orden,request):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class modelo18Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user_id,orden,fecha_ano):
        response = self.filter(usuario_id=user_id,numeral__orden=orden,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def generarPdf(self,user_id,fecha_ano):
        response = self.filter(usuario_id=user_id, periodo__fecha_inicio__year = fecha_ano)
        return response

    def entradasContador(self,year,orden,request):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral__orden=orden,
        usuario__coordinacion_id=request.user.coordinacion_id).count())
        return response
    
    def anexo(self,user_id,year):
        response = self.exclude(anexo= "").filter(usuario_id = user_id, periodo__fecha_inicio__year= year)
        return response

class citasManager(models.Manager):
    def reporteProductividad(self,user_id):
        response = self.filter(usuario_id=user_id)
        return response

    def generarPdf(self,user_id):
        response = self.filter(usuario_id=user_id)
        return response
      
    def anexo(self,user_id):
        response = self.exclude(anexo= "").filter(usuario_id = user_id)
        return response

class glosarioManager(models.Manager):
    def reporteProductividad(self,seccion):
        response = self.filter(seccion=seccion)
        return response



