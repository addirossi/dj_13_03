from django.db import models
# from django.utils.text import slugify
from pytils.translit import slugify


class Publisher(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, unique=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    year = models.PositiveSmallIntegerField(default=1)
    slug = models.SlugField(max_length=100, primary_key=True)

    def __str__(self):
        return self.title

    def save(self):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save()


class Order(models.Model):
    address = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book, through='OrderItems')

    def __str__(self):
        return f'Заказ №{self.id}'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    quantity = models.PositiveSmallIntegerField(default=1)


# order = Order.objects.get(id=1)
# order.items.first()