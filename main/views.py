from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView

from main.models import Book


class BooksListView(ListView):
    queryset = Book.objects.all()
    template_name = 'main/list.html'
    context_object_name = 'books'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset


class BookDetailsView(View):
    def get(self, request, book_slug):
        # try:
        #     book = Book.objects.get(slug=book_slug)
        #     return render(request, 'main/details.html', {'book': book})
        # except Book.DoesNotExist:
        #     raise Http404('Книга не найдена')
        book = get_object_or_404(Book, slug=book_slug)
        return render(request, 'main/details.html', {'book': book})
