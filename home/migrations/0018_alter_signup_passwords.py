# Generated by Django 4.1.3 on 2023-01-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_alter_signup_passwords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='passwords',
            field=models.CharField(default="{'Facebook':None,'Instagram':None,'Twitter':None,'Dropbox':None,'Google':None,'Spotify':None,'GitHub':None,'Snapchat':None}", max_length=10000000),
        ),
    ]
