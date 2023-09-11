from .models import *
from rest_framework import serializers


class CompanyApi(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_title','address','phone_no']
        
        
class EmployeeApi(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
        
        
class RoleApi(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
        
        
class AssetApi(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '__all__'
        
        
class AssetTrackingApi(serializers.ModelSerializer):
    class Meta:
        model = AssetTrack
        fields = '__all__'