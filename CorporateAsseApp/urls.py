from . import views
from django.urls import path, include


urlpatterns = [
    path('company/', views.CompanyView.as_view({'get': 'get',
                                                'post':'create'})),
]
