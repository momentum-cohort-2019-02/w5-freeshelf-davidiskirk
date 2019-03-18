from django.shortcuts import render
from catalog.models import Book, Category
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
def base(request):
    book_list = Book.objects.all()

    context = {
        'book_list': book_list,
        
    }

    
    return render(request, 'base.html', context=context)


from django.views import generic

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 10

class CategoryListView(generic.ListView):
    model = Category
    

class CategoryDetailView(generic.DetailView):
    model = Category

@require_http_methods(['POST'])
@login_required
def book_favorite_view(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)

    # Toggle whether or not book is favorited

    favorite, created = request.user.favorited_books.get_or_create(book=book)

    if created:
        messages.success(request, f"You have favorited {book.title}.")
    else:
        messages.info(request, f"You have unfavorited {book.title}.")
        favorite.delete()

    return redirect(book.get_absolute_url())
