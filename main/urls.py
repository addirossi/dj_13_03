from datetime import datetime

from django.urls import path, register_converter

from main.views import BooksListView, BookDetailsView

# class DateConverter:
#    regex = r'[0-9]{4}-[0-9]{2}-[0-9]{2}'
#    format = '%Y-%m-%d'
#
#    def to_python(self, value: str) -> datetime:
#        return datetime.strptime(value, self.format)
#
#    def to_url(self, value: datetime) -> str:
#        return value.strftime(self.format)
#
# register_converter(DateConverter, 'yyyy-mm-dd')

urlpatterns = [
    path('books/', BooksListView.as_view(), name='books-list'),
    path('books/<slug:book_slug>/', BookDetailsView.as_view(), name='book-details'),
    # path('books/<yyyy-mm-dd:date>/', ...)
]

# books/yyyy-mm-dd