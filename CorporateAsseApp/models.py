from django.db import models

# Create your models here.

class Company(models.Model):
    company_title = models.CharField(max_length=300)
    address = models.CharField(max_length=550, blank=True, null=True)
    phone_no = models.IntegerField(blank=True, null=True)
    
    def __str__(self) -> str:
        return self.company_title
    
    class Meta:
        verbose_name_plural = 'Companies'
    
class Assets(models.Model):
    title = models.CharField(max_length=350)
    details = models.TextField(blank=True, null=True)
    company_asset = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='Company_Asset')
    
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Assets'
        
        
class Role(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.title
        
class Employees(models.Model):
    employee_name = models.CharField(max_length=400)
    company_employee = models.ForeignKey(Company, on_delete=models.CASCADE)
    roles = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='Employee_Role')
    
    def __str__(self) -> str:
        return self.employee_name
    
    class Meta:
        verbose_name_plural = 'Employees'
        
        
class AssetTrack(models.Model):
    title = models.CharField(max_length=100)
    asset = models.ManyToManyField(Assets)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name='Assign_Assets')
    condition_at_checkout = models.CharField(max_length=200, blank=True, null=True)
    condition_at_return = models.CharField(max_length=200, blank=True, null=True)
    checkout_at = models.DateField()
    returned_at = models.DateField(blank=True, null=True)
    is_returned = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Assets Track Record'
    