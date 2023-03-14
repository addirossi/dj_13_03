from django.urls import path

from main.views import BooksListView, BookDetailsView

urlpatterns = [
    path('books/', BooksListView.as_view(), name='books-list'),
    path('books/<slug:book_slug>/', BookDetailsView.as_view(), name='book-details'),
]
