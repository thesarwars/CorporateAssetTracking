from .models import *
from rest_framework import serializers


class CompanyApi(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['company_title','address','phone_no']
        
        
class EmployeeApi(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '_all_'
        
        
class RoleApi(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '_all_'
        
        
class AssetApi(serializers.ModelSerializer):
    class Meta:
        model = Assets
        fields = '_all_'
        
        
class AssetTrackingApi(serializers.ModelSerializer):
    class Meta:
        model = AssetTrack
        fields = '_all_'