# Generated by Django 2.1.7 on 2019-03-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_remove_book_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]