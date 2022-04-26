from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from apissys.app.ssysemployee.api import viewsets


route = routers.DefaultRouter()
route.register(r'employees', viewsets.Employees_ViewSet, basename='Employees')
route.register(r'reports/employees/age', viewsets.Age_Reports_ViewSet, basename='Age')
route.register(r'reports/employees/salary', viewsets.Salary_Reports_ViewSet, basename='Salary')


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(route.urls)),
]
