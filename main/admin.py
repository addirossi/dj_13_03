from django import forms
from django.contrib import admin

from .models import Publisher, Book, Order, OrderItems

# class RelationshipInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         count = 0
#         for form in self.forms:
#             if form.cleaned_data['is_main']:
#                 count += 1
#         if count > 1:
#             raise forms.ValidationError('Только один тэг может быть основным')
#         return super().clean()


class BookAdminForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publisher', 'year']

    # def clean(self):
    #     year = self.cleaned_data.get('year')
    #     if year > 2023:
    #         raise forms.ValidationError('Неверный год')
    #     return super().clean()

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year > 2023:
            raise forms.ValidationError('Неверный год')
        return year

    # def validate_year(self, year):
    #     if year > 2023:
    #         raise serializers.ValidationError('')
    #     return year

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
