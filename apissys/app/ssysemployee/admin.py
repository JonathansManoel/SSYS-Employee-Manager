from django.contrib import admin
from .models import Employees


# Register your models here.
class Employees_Admin(admin.ModelAdmin):
    # Listar o que aparecer no admin
    list_display = ('id', 'name', 'email', 'department', 'salary', 'birth_date')
    # Filtros
    list_filter = ('birth_date', 'salary')
    fieldsets = (
        (u'EMPLOYEES / DETAIL', {'fields': ('name', 'email', 'department', 'salary', 'birth_date')}),
    )


# Registro Models
admin.site.register(Employees, Employees_Admin)
