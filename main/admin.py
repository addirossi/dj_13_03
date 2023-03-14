from django import forms
from django.contrib import admin

from .models import Publisher, Book, Order, OrderItems


class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publisher', 'year']


class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    list_display = ['title', 'publisher']


class OrderItemsInline(admin.TabularInline):
    model = OrderItems


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]
    list_display = ['id', 'address']


admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItems)
