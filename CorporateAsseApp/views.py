from django.shortcuts import render, HttpResponse
from . models import Company, Employees, Role, Assets, AssetTrack
from . serializers import CompanyApi, EmployeeApi, RoleApi, AssetApi, AssetTrackingApi
from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
import json

# Create your views here.
def index(request):
    return HttpResponse('Hello Tahasin')


class CompanyView(viewsets.ViewSet):
    def get(self, request):
        try:
            print(request.data)
            company = Company.objects.all()
            serializer = CompanyApi(company, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return HttpResponse(json.dumps({'error': str(e)}), content_type="application/json")
            
    def create(self, request):
        serializer = CompanyApi(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class RoleView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleApi
    
    
# class EmployeeView(viewsets.ViewSet):
#     def get(self, request):
#         print("Employees Data",request.data)
#         employee = Employees.objects.all()
#         serializer = EmployeeApi(employee, many = True)