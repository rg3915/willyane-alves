# Generated by Django 3.1.2 on 2020-11-14 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_service', '0010_remove_serviceitem_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerservice',
            name='discount',
            field=models.IntegerField(blank=True, choices=[(0.05, '5%'), (0.1, '10%'), (0.15, '15%'), (0.2, '20%')], verbose_name='Desconto'),
        ),
    ]
