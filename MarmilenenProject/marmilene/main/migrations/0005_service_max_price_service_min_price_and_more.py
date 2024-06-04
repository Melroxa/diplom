# Generated by Django 5.0.3 on 2024-05-19 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_service_options_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='max_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Максимальная цена'),
        ),
        migrations.AddField(
            model_name='service',
            name='min_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Минимальная цена'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена'),
        ),
    ]