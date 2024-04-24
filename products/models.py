from django.utils import timezone

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    brand = models.ForeignKey(
        'products.Brand', on_delete=models.CASCADE,
        related_name='products'
    )

    image = models.ImageField(
        blank=True, null=True,
        upload_to='media/products/'
    )

    discount = models.IntegerField()

    created_at = models.DateTimeField(
        default=timezone.now
    )
    published_at = models.DateTimeField(
        blank=True, null=True
    )

    def __str__(self):
        return f'{self.name} | {self.brand}'


class Brand(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True, blank=True)

    logo = models.ImageField(
        blank=True, null=True,
        upload_to='media/products/'
    )

    created_at = models.DateTimeField(
        default=timezone.now
    )
    published_at = models.DateTimeField(
        blank=True, null=True
    )

    def __str__(self):
        return self.name

