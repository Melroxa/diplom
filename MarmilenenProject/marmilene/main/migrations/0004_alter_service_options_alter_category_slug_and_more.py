# Generated by Django 5.0.3 on 2024-05-19 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_category_options_alter_master_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('title',), 'verbose_name': 'Цена на услугу', 'verbose_name_plural': 'Цены на услуги'},
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL'),
        ),
    ]
