# Generated by Django 4.1.3 on 2023-01-14 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_alter_signup_passwords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='image',
            field=models.ImageField(default='img19_1920x1200.jpg', upload_to='images/downloaded'),
        ),
    ]
