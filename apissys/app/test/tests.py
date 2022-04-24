"""
import pytest
from rest_framework.reverse import reverse
from apissys.app.ssysemployee.api.viewsets import Employees_ViewSet
from .models import Employees
from django.test import TestCase
from rest_framework.test import APIClient


@pytest.fixture
def employees(usuario):
    return usuario.Employees_ViewSet.get(reverse('rest_framework:login'))


def teste_usuario_logado(employees):
    assert employees.status_code == 200


class ModelTestCase(TestCase):
    def setUp(self):
        self.employeelist_name = "Anakin Skywalker"
        self.employeelist = Employees(name=self.employeelist_name)


class ViewTestCase(TestCase):

    def create(self):
        self.client = APIClient()
        self.employees = {'name': 'Anakin Skywalker', 'email': 'skywalker@ssys.com.br',
                                  'department': 'Architecture'}
        self.response = self.client.post(
            reverse('create'),
            self.employees,
            format="json")
"""