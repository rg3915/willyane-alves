# Generated by Django 3.1.2 on 2020-11-19 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0031_auto_20201119_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceitem',
            name='customerservice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='serviceitem', to='customer_service.customerservice'),
        ),
    ]
