from rest_framework import viewsets
from apissys.app.ssysemployee.api import serializers
from apissys.app.ssysemployee import models
from rest_framework.permissions import IsAuthenticated


class Employees_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Employees_Serializer
    permission_classes = (IsAuthenticated,)
    queryset = models.Employees.objects.all()

    def get_view_name(self):
        return "SSYS Employee"


class Age_Reports_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Age_Reports_Serialazer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = models.Employees.objects.all().order_by('birth_date')
        younger = queryset.first()
        older = queryset.last()
        return younger, older

    def get_view_name(self):
        return "Age Report"


class Salary_Reports_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Salary_Reports_Serialazer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = models.Employees.objects.all().order_by('salary')
        lowest = queryset.first()
        highest = queryset.last()
        return lowest, highest

    def get_view_name(self):
        return "Salary Report"
