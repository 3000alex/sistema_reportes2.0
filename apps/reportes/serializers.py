from rest_framework import serializers
from .models import (Modelo1, Modelo2, Modelo3, Modelo4, Modelo5, Modelo6, Modelo7, Modelo8, Modelo9, Modelo10,
                     Modelo11, Modelo12, Modelo13, Modelo14, Modelo15, Modelo16, Modelo17, Modelo18, Citas, Numeral,ReporteEnviado,Periodo)


class NumeralesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numeral
        fields = "__all__"

class PeriodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = "__all__"

class Modelo1Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo1
        fields = '__all__'

class Modelo2Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo2
        fields = "__all__"

class Modelo3Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo3
        fields = "__all__"

class Modelo4Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo4
        fields = "__all__"

class Modelo5Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo5
        fields = "__all__"

class Modelo6Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo6
        fields = "__all__"

class Modelo7Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo7
        fields = "__all__"

class Modelo8Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo8
        fields = "__all__"

class Modelo9Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo9
        fields = "__all__"

class Modelo10Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo10
        fields = "__all__"

class Modelo11Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo11
        fields = "__all__"

class Modelo12Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo12
        fields = "__all__"

class Modelo13Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo13
        fields = "__all__"

class Modelo14Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo14
        fields = "__all__"

class Modelo15Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo15
        fields = "__all__"

class Modelo16Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo16
        fields = "__all__"

class Modelo17Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo17
        fields = "__all__"

class Modelo18Serializer(serializers.ModelSerializer):
    numeral = NumeralesSerializer(many=False, read_only=True)
    numeral_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Modelo18
        fields = "__all__"

class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields = "__all__"

class ReportesSerializer(serializers.ModelSerializer):
    periodo = PeriodosSerializer(many=False, read_only=True)
    class Meta:
        model = ReporteEnviado
        fields = "__all__"