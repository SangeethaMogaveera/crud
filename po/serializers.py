from rest_framework import serializers
from .models import Po

class PoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Po
        fields = '__all__'
        #fields='client_name','client_type','client_alias',

