from django.urls import path
from . import views
from catalog import views as core_views



urlpatterns = [
    path('', views.base, name='base'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('categories/<int:pk>', views.CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail'),
    path('book/<int:book_pk>/favorite/', core_views.book_favorite_view, name="book_favorite")
]
    
