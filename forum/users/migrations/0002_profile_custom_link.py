# Generated by Django 4.0.4 on 2022-05-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='custom_link',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
