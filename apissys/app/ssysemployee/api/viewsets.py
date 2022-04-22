from rest_framework import viewsets
from apissys.app.ssysemployee.api import serializers
from apissys.app.ssysemployee import models


class Employees_ViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.Employees_Serializer
    queryset = models.Employees.objects.all()
