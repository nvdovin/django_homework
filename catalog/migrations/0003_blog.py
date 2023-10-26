# Generated by Django 4.2.5 on 2023-10-24 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_category_alter_product_creations_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=30, verbose_name='Slug')),
                ('content', models.CharField(max_length=50, verbose_name='Содержимое')),
                ('preview', models.ImageField(upload_to='catalog/media', verbose_name='Превью')),
                ('creation_date', models.DateField(auto_now=True, verbose_name='Дата сощдания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Статус публикации')),
                ('views_counter', models.IntegerField(verbose_name='Счетчик просморов')),
            ],
            options={
                'verbose_name': 'Блог для сайта',
                'verbose_name_plural': 'Блоги для сайта',
            },
        ),
    ]