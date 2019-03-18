from django.db import models

from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

   
    author = models.CharField(max_length=100, null=True)
    
    summary = models.TextField(max_length=1000, null=True)
    
    website = models.CharField(max_length=100, null=True)

    date_added = models.DateField(null=True, blank=True )

    category = models.CharField(max_length=100, null=True)

    slug = models.SlugField(null=True, blank=True)

    def get_slug(self):
        if self.slug:
            return
        self.slug = slugify(self.title)

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        if self.slug:
            return

        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        while Book.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)

        self.slug = slug
    

    
    class Meta:
        ordering = ['-date_added']


    def __str__(self):
       
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])


class Category(models.Model):
    """Model for programming languages"""
    language = models.CharField(max_length=100)

    # making slug
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)

    def set_slug(self):
        if self.slug:
            return

        base_slug = slugify(self.language)
        slug = base_slug
        n = 0

        while Category.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)

        self.slug = slug

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])

    def __str__(self):
        return self.language

   
