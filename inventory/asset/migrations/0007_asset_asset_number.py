# Generated by Django 3.1.6 on 2021-02-15 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0006_auto_20210212_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='asset_number',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
