# Generated by Django 2.1.1 on 2018-09-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('description', models.TextField(blank=True)),
                ('rules', models.TextField(blank=True)),
                ('blacklist', models.ManyToManyField(related_name='blacklist', to='profile.Profile')),
                ('moderators', models.ManyToManyField(related_name='moderators', to='profile.Profile')),
                ('subscribers', models.ManyToManyField(related_name='subscribers', to='profile.Profile')),
            ],
        ),
    ]
