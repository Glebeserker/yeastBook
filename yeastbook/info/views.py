from curses.ascii import HT
from django.db.models import Q
from django.http import Http404
from .serializers import CompaniesSerializer, TypesSerializer, YeastCompaniesSerializer, YeastSerializer, YeastTypeSerializer
from .models import YeastCompany, Yeast, YeastType

from rest_framework.views import APIView
from rest_framework.response import Response

class CompanyView(APIView):

    def get(self, request, format = None):
        comapny = YeastCompany.objects.all()
        serializer = CompaniesSerializer(comapny, many = True)
        return Response(serializer.data)
    
class TypeView(APIView):
    
    def get(self, request, format = None):
        types = YeastType.objects.all()
        serializer = TypesSerializer(types, many = True)
        return Response(serializer.data)
    
class AllYeast(APIView):
    
    def get(self, request, format = None):
        yeast = Yeast.objects.all()
        serializer = YeastSerializer(yeast, many = True)
        return Response(serializer.data)

class AllDetailYeast(APIView):

    def get_object(self, yeast_slug):
        try:
            return Yeast.objects.get(slug = yeast_slug)
        except Yeast.DoesNotExist:
            raise Http404

    def get(self, request, yeast_slug, format=None):
        yeast = self.get_object(yeast_slug)
        serializer = YeastSerializer(yeast)
        return Response(serializer.data)
    
class CompanyFilteredView(APIView):
    
    def get_object(self, company_slug):
        try:
            return YeastCompany.objects.get(slug = company_slug)
        except Yeast.DoesNotExist:
            raise Http404
        
    def get(self, request, company_slug ,format = None):
        company = self.get_object(company_slug)
        serializer = YeastCompaniesSerializer(company)
        return Response(serializer.data)

class TypeFilteredView(APIView):
    
    def get_object(self, type_slug):
        try:
            return YeastType.objects.get(slug = type_slug)
        except YeastType.DoesNotExist:
            raise Http404
        
    def get(self, request, type_slug,  format=None):
        types = self.get_object(type_slug)
        serializer = YeastTypeSerializer(types)
        return Response(serializer.data)
    
class TypedYeastView(APIView):
    
    def get_object(self, type_slug, yeast_slug):
        try: 
            return Yeast.objects.filter(yeast_type__slug = type_slug).get(slug = yeast_slug)
        except Yeast.DoesNotExist:
            raise Http404
        
    def get(self, request ,type_slug, yeast_slug, format=None):
        yeast = self.get_object(type_slug, yeast_slug)
        serializer = YeastSerializer(yeast)
        return Response(serializer.data)
    
class CompanyYeastView(APIView):
    
    def get_object(self, company_slug, yeast_slug):
        try:
            return Yeast.objects.filter(company__slug = company_slug).get(slug=yeast_slug)
        except Yeast.DoesNotExist:
            raise Http404
        
    def get(self, request,company_slug, yeast_slug,  format=None):
        yeast = self.get_object(company_slug, yeast_slug)
        serializer = YeastSerializer(yeast)
        return Response(serializer.data)
