# Generated by Django 2.2.3 on 2019-07-17 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20190718_0235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first',
            name='submission',
            field=models.DateField(verbose_name='submitted date'),
        ),
    ]