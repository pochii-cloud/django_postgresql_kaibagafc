# Generated by Django 3.2.5 on 2021-08-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testpost', '0010_alter_mymessage_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='Joined',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=50)),
                ('age', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=100)),
                ('phone', models.PositiveIntegerField(max_length=20)),
                ('previous_club', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='MyMessage',
        ),
    ]