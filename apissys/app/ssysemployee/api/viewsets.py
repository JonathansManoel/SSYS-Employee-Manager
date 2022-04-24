from rest_framework import viewsets
from apissys.app.ssysemployee.api import serializers
from apissys.app.ssysemployee import models
from rest_framework.permissions import IsAuthenticated


class Employees_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Employees_Serializer
    permission_classes = (IsAuthenticated,)
    queryset = models.Employees.objects.all()


class Age_Reports_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Age_Reports_Serialazer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        younger = models.Employees.objects.all().order_by('birth_date').first()
        older = models.Employees.objects.all().order_by('birth_date').last()
        return younger, older


class Salary_Reports_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Salary_Reports_Serialazer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        lowest = models.Employees.objects.all().order_by('salary').first()
        highest = models.Employees.objects.all().order_by('salary').last()
        return lowest, highest
