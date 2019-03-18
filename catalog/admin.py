from django.contrib import admin

# Register your models here.
from catalog.models import Book, Category

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(BookInstance)
admin.site.register(Category)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')