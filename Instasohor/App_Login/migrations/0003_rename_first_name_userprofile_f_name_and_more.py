# Generated by Django 4.0.6 on 2022-07-11 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0002_rename_profile_pic_userprofile_profile_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='first_name',
            new_name='f_name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='last_name',
            new_name='l_name',
        ),
    ]
