# Generated by Django 3.1.6 on 2021-02-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='asset_category',
            field=models.CharField(max_length=200),
        ),
    ]
