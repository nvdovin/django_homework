# Generated by Django 4.2.5 on 2023-12-22 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='creations_date',
            field=models.DateField(auto_created=True, auto_now_add=True, verbose_name='Дата создания'),
        ),
    ]
