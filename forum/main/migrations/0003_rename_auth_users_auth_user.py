# Generated by Django 4.0.4 on 2022-04-27 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_users_auth_users'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auth_Users',
            new_name='Auth_User',
        ),
    ]
