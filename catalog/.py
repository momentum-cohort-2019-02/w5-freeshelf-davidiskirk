from django.db import migrations
from django.conf import settings
import os.path
import csv
from django.core.files import File

def load_book_data(apps, schema_editor):
    """red a CSV file full of books and insert them into the datatbase """

    Book = apps.get_model ('catalog', 'Book')
    datapath = os.path.join(settings.BASE_DIR, 'initial_data')
    datafile = os.path.join(datapath, 'Books.csv')
    with open (datafile) as file:
        reader= csv.DictReader(file)
        for row in reader:
            title = row['title']
            if Book.object.filter(title=title).count():
                continue
            book = Book(
                title=row['title'],
                author=row['author'],
                category=row['category'],
                summary=row['summary'],
                website=row['website'],
                date_added=row['date_added'],


            )
            book.save()


 

class Migration(migrations.Migration):

    dependencies = [
        ('catalog','009_book_picture' )
    ]

    operations = [
        migrations.RunPython(load_book_data),
    ]