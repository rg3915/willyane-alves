# Generated by Django 3.1.2 on 2020-11-06 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0011_auto_20201106_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='picture',
            field=models.ImageField(blank=True, upload_to='pictures/%Y/%m/', verbose_name='Foto'),
        ),
    ]