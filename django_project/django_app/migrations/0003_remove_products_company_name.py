# Generated by Django 5.0.1 on 2024-02-10 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_app', '0002_alter_products_options_products_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='company_name',
        ),
    ]
