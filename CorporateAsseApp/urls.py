from . import views
from django.urls import path, include


urlpatterns = [
    path('company/', views.CompanyView.as_view({'get': 'get',
                                                'post':'create'})),
    path('create-role/', views.RoleView.as_view()),
    path('employee/', views.EmployeeView.as_view({'get': 'get', 'post': 'create'})),
    path('asset/', views.AssetView.as_view({'get': 'get', 'post': 'create'})),
    path('asset-track/', views.AssetTrackingView.as_view({'get': 'get', 'post': 'create'})),
    
]
