from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    department = models.CharField(max_length=255, null=False)
    salary = models.DecimalField(max_digits=13, editable=True, null=True, decimal_places=2)
    birth_date = models.DateField(auto_now_add=False, editable=True)

    class Meta:
        verbose_name = u'Employees'
        ordering = ['id']

    def __int__(self):
        return f'{self.id}'
