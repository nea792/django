# Generated by Django 2.2.12 on 2021-08-30 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='defualt.jpeg', upload_to='pics'),
        ),
    ]
