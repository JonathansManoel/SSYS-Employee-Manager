# Generated by Django 4.0.4 on 2022-04-22 07:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('salary', models.IntegerField()),
                ('birth_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Employees',
                'ordering': ('id',),
            },
        ),
    ]
