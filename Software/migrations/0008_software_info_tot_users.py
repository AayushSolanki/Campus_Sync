# Generated by Django 3.2.8 on 2022-02-25 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Software', '0007_auto_20220225_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='software_info',
            name='Tot_users',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
