# Generated by Django 3.1.2 on 2020-11-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0018_remove_customerservice_serviceitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerservice',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Data'),
        ),
    ]
