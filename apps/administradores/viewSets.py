from rest_framework import viewsets
from ..registration.models import User  
from apps.reportes.models import ReporteEnviado
from .serializers import InvestigadoresSerializer,ReportesAdmSerializer
from rest_framework import status
from rest_framework.response import Response
from django.utils.crypto import get_random_string
from apps.reportes.models import Citas
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

class InvestigadoresViewSet(viewsets.ModelViewSet):
    serializer_class = InvestigadoresSerializer
    queryset = User.objects.filter(is_staff=False)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, validated_data):
        
        password = get_random_string(length=20)
        registro = {}
        user = User(
            email=validated_data._data['email'],
            nombre = validated_data._data['nombre'],
            apellido = validated_data._data['apellido'],
            nombreCorto = validated_data._data['nombreCorto'],
        )
        
        user.set_password(password)
        user.save()
        
        Citas.objects.create(numeral_id = 31,  usuario_id = user.id)

        body = render_to_string(
            'administradores/templateBienvenida.html', {
                'nombre': user.first_name,
                'apellido': user.apellido,
                'password': password,
                'correo': user.email,
            },
        )

        email_message = EmailMessage(
            subject='Bienvenido(a) al Sistema de Reportes de Astrofísica',
            body=body,
            from_email='reportes-astro@inaoep.mx',
            to=[user.email],#,'reportes-astro@inaoep.mx'],
        )
        email_message.content_subtype = 'html'
        email_message.send()
        
        if user: 
            registro['creado'] = 'El usuario fue creado exitosamente'
       
        return Response(registro, status=status.HTTP_201_CREATED)
        
        #return Response(user, status=status.HTTP_201_CREATED)


class ReportesAdmViewSet(viewsets.ModelViewSet):
    serializer_class = ReportesAdmSerializer
    queryset = ReporteEnviado.objects.all()

    def list(self, request, *args, **kwargs):
        query_set = ReporteEnviado.objects.filter(periodo_id=self.request.GET['periodo'])
        serializer = self.get_serializer(query_set, many=True)
        return Response(serializer.data)

