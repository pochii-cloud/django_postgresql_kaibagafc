# Generated by Django 3.2.5 on 2021-08-07 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testpost', '0005_remove_room_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='room_name',
            new_name='name',
        ),
    ]