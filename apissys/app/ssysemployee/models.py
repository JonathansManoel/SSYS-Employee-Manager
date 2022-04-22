from django.db import models


# Create your models here.
class Employees(models.Model):
    id = models.BigIntegerField(primary_key=True, editable=True)
    name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    department = models.CharField(max_length=255, null=False, blank=False)
    salary = models.IntegerField(auto_created=True, editable=True)
    birth_date = models.DateField(auto_created=True, editable=True)

    class Meta:
        verbose_name = u'Employees'
        ordering = ('id',)

    def __int__(self):
        return self.id
