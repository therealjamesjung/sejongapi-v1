# Generated by Django 2.1.1 on 2018-09-14 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='moderators',
            field=models.ManyToManyField(related_name='moderators', to='profile.Profile'),
        ),
    ]
