# Generated by Django 4.1.7 on 2023-04-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_profile_avatar_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=140, null=True),
        ),
    ]
