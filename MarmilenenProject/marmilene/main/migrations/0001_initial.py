# Generated by Django 5.0.3 on 2024-05-11 02:17

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CategoryMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя мастера')),
                ('slug', models.SlugField(null=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, default='images/thumbnails/unnamed.jpg', upload_to='images/cat_lookbook/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))], verbose_name='Фото мастера')),
            ],
            options={
                'verbose_name': 'Категория мастера',
                'verbose_name_plural': 'Категории мастеров',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Lookbook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='ФИО')),
                ('experience', models.CharField(max_length=20, verbose_name='Стаж рааботы')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, default='images/thumbnails/unnamed.jpg', upload_to='images/lookbook/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))], verbose_name='Фото услуг')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='main.categorymaster', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'мастер',
                'verbose_name_plural': 'мастера',
                'ordering': ('title',),
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('slug', models.SlugField(max_length=200, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цены')),
                ('available', models.BooleanField(default=True, verbose_name='Действующая услуга')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='main.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Цена',
                'verbose_name_plural': 'Цены',
                'ordering': ('title',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
