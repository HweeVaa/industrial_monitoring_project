# Generated by Django 3.2.5 on 2022-02-28 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonitoringApp', '0002_alter_health_heartrate'),
    ]

    operations = [
        migrations.CreateModel(
            name='environment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gas_voltage_level', models.FloatField(max_length=20)),
                ('LPG_ppm', models.FloatField(max_length=20)),
                ('CO_ppm', models.FloatField(max_length=20)),
                ('time', models.DateTimeField(max_length=20)),
            ],
        ),
    ]
