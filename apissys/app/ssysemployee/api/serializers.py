from rest_framework import serializers
from apissys.app.ssysemployee import models


class Employees_Serializer(serializers.ModelSerializer):
    class Meta:
        verbose_name = "Employees"
        model = models.Employees
        fields = '__all__'


class Age_Reports_Serialazer(serializers.ModelSerializer):
    class Meta:
        verbose_name = "Age"
        model = models.Employees
        fields = '__all__'


class Salary_Reports_Serialazer(serializers.ModelSerializer):
    class Meta:
        verbose_name = "Salary"
        model = models.Employees
        fields = '__all__'
