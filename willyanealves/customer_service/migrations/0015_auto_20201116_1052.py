# Generated by Django 3.1.2 on 2020-11-16 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0014_auto_20201116_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerservice',
            name='service_item',
        ),
        migrations.AlterField(
            model_name='serviceitem',
            name='customerservice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='customer_service.customerservice'),
        ),
    ]
