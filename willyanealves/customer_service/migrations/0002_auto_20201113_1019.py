# Generated by Django 3.1.2 on 2020-11-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerservice',
            name='discount',
            field=models.IntegerField(blank=True, verbose_name='Desconto'),
        ),
    ]
