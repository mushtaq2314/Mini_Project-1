# Generated by Django 4.1.3 on 2022-12-10 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_signup_passwords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='phone',
            field=models.IntegerField(),
        ),
    ]