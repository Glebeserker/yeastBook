from dataclasses import field
from rest_framework import serializers

from .models import YeastCompany, YeastType, Yeast

class TypesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = YeastType
        fields = (
            'id',
            'name',
            'return_absolute_url',
        )
        
class CompaniesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = YeastCompany
        fields = (
            'id',
            'name',
            'return_absolute_url',
        )
        
class YeastSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Yeast
        fields = (
            'id',
            'name',
            'return_absolute_url',
            'gen_info',
            'sec_info',
        )
        
class YeastCompaniesSerializer(serializers.ModelSerializer):
    yeasts = YeastSerializer(many=True,)
    
    class Meta:
        model = YeastCompany
        fields = (
            'id',
            'name',
            'return_absolute_url',
            'yeasts',
        )
        
class YeastTypeSerializer(serializers.ModelSerializer):
    yeastss = YeastSerializer(many=True,)
    
    class Meta:
        model = YeastType
        fields = (
            'id',
            'name',
            'return_absolute_url',
            'yeastss',
        )