from rest_framework import serializers
from .models import usuario


class UsuarioSerializer(serializers.ModelSerializer):
        class Meta:
            model = usuario
            fields=('id','Nombres','Apaterno','Amaterno','Edad')


                   