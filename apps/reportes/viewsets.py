from .serializers import (Modelo1Serializer, Modelo2Serializer, Modelo3Serializer, Modelo4Serializer, Modelo5Serializer, Modelo6Serializer, Modelo7Serializer, Modelo8Serializer, Modelo9Serializer, Modelo10Serializer,
                          Modelo11Serializer, Modelo12Serializer, Modelo13Serializer, Modelo14Serializer, Modelo15Serializer, Modelo16Serializer, Modelo17Serializer, Modelo18Serializer, CitasSerializer, NumeralesSerializer, ReportesSerializer)

from .models import (Modelo1, Modelo2, Modelo3, Modelo4, Modelo5, Modelo6, Modelo7, Modelo8, Modelo9, Modelo10, Modelo11, Modelo12, Modelo13, Modelo14, Modelo15, Modelo16,
                     Modelo17, Modelo18, Numeral, Citas, Periodo, ReporteEnviado)
# rest-framework
from rest_framework import viewsets
from rest_framework.response import Response
from sistema_reportes.settings import BASE_DIR
import os


class Numerales(viewsets.ModelViewSet):
    serializer_class = NumeralesSerializer
    queryset = Numeral.objects.all()

class modelo1(viewsets.ModelViewSet):
    serializer_class = Modelo1Serializer
    queryset = Modelo1.objects.all()
    
    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_biblioteca = self.request.GET['biblioteca']
        
        if query_biblioteca:
            query_set = Modelo1.objects.biblioteca_astrofisica(id)
        else: 
            query_set = Modelo1.objects.all()
            
        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo2(viewsets.ModelViewSet):
    serializer_class = Modelo2Serializer
    queryset = Modelo2.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo2.objects.reporteProductividad()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo3(viewsets.ModelViewSet):
    serializer_class = Modelo3Serializer
    queryset = Modelo3.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo3.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo4(viewsets.ModelViewSet):
    serializer_class = Modelo4Serializer
    queryset = Modelo4.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo4.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo5(viewsets.ModelViewSet):
    serializer_class = Modelo5Serializer
    queryset = Modelo5.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo5.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo6(viewsets.ModelViewSet):
    serializer_class = Modelo6Serializer
    queryset = Modelo6.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo6.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo7(viewsets.ModelViewSet):
    serializer_class = Modelo7Serializer
    queryset = Modelo7.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo7.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)


class modelo8(viewsets.ModelViewSet):
    serializer_class = Modelo8Serializer
    queryset = Modelo8.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo8.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo9(viewsets.ModelViewSet):
    serializer_class = Modelo9Serializer
    queryset = Modelo9.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo9.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo10(viewsets.ModelViewSet):
    serializer_class = Modelo10Serializer
    queryset = Modelo10.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo10.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo11(viewsets.ModelViewSet):
    serializer_class = Modelo11Serializer
    queryset = Modelo11.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo11.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo12(viewsets.ModelViewSet):
    serializer_class = Modelo12Serializer
    queryset = Modelo12.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo12.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo13(viewsets.ModelViewSet):
    serializer_class = Modelo13Serializer
    queryset = Modelo13.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo13.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo14(viewsets.ModelViewSet):
    serializer_class = Modelo14Serializer
    queryset = Modelo14.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo14.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo15(viewsets.ModelViewSet):
    serializer_class = Modelo15Serializer
    queryset = Modelo15.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo15.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo16(viewsets.ModelViewSet):
    serializer_class = Modelo16Serializer
    queryset = Modelo16.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo16.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class modelo17(viewsets.ModelViewSet):
    serializer_class = Modelo17Serializer
    queryset = Modelo17.objects.all()

class modelo18(viewsets.ModelViewSet):
    serializer_class = Modelo18Serializer
    queryset = Modelo18.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Modelo18.objects.listarBiblioteca()

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class citas(viewsets.ModelViewSet):
    serializer_class = CitasSerializer
    queryset = Citas.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = Citas.objects.all

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

class reportes_finalizados(viewsets.ModelViewSet):
    serializer_class = ReportesSerializer
    queryset = ReporteEnviado.objects.all()

    def list(self, request, *args, **kwargs):
        id = self.request.GET['id_usuario']
        query_set = ReporteEnviado.objects.filter(usuario_id=id)

        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)