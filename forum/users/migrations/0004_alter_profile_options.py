# Generated by Django 4.0.4 on 2022-05-04 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_custom_link_profile_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Профиль пользователя', 'verbose_name_plural': 'Профили пользователей'},
        ),
    ]