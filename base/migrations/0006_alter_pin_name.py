# Generated by Django 5.0.1 on 2024-02-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_pin_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
