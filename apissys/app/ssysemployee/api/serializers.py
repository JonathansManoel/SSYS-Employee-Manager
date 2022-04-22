from rest_framework import serializers
from apissys.app.ssysemployee import models


class Employees_Serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employees
        fields = ('id', 'name', 'email', 'department', 'salary', 'birth_date',)
