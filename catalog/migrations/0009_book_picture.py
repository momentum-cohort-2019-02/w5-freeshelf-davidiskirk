# Generated by Django 2.1.7 on 2019-03-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_auto_20190313_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(null=True, upload_to='bookpics/'),
        ),
    ]
