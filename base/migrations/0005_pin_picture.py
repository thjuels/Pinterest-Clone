# Generated by Django 5.0.1 on 2024-02-04 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_pin_tags_pin_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='picture',
            field=models.ImageField(default='avatar.svg', upload_to=''),
        ),
    ]
