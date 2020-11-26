from rest_framework import serializers
from ..registration.models import User
from apps.reportes.models import ReporteEnviado

class InvestigadoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','nombre','apellido','email','nombreCorto','categoria','nivelSni','orcId','arxivId']


class ReportesAdmSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteEnviado
        fields = "__all__"