# Generated by Django 4.1.7 on 2023-04-08 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
