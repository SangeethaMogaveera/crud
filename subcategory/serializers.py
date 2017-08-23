from rest_framework import serializers
from .models import Subcategory

class SubCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = '__all__'

