# Generated by Django 2.1.7 on 2019-03-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_book_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='date',
        ),
        migrations.AddField(
            model_name='book',
            name='date_added',
            field=models.DateField(blank=True, null=True),
        ),
    ]
