# Generated by Django 4.0.3 on 2022-04-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Software', '0013_alter_software_info_purforsub_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software_info',
            name='Pur_from',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='software_info',
            name='order_ref',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='software_info',
            name='spec',
            field=models.CharField(max_length=1000),
        ),
    ]
