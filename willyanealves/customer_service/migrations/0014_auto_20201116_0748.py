# Generated by Django 3.1.2 on 2020-11-16 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
        ('customer_service', '0013_auto_20201116_0739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceitem',
            name='customer',
        ),
        migrations.AlterField(
            model_name='customerservice',
            name='service_item',
            field=models.ManyToManyField(related_name='customeritem', through='customer_service.ServiceItem', to='services.Service'),
        ),
    ]
