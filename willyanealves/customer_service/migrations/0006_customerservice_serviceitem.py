# Generated by Django 3.1.2 on 2020-11-14 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0005_auto_20201114_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerservice',
            name='serviceitem',
            field=models.ManyToManyField(to='customer_service.ServiceItem'),
        ),
    ]
