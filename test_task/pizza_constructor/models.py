from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=200)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

#     @property
#     def get_price(self):
#         return self.price
#
#
# class OrderItems(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)
#
#     quantity = models.PositiveIntegerField(default=0)
#     total_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
#
#     @property
#         # def price(self):
#         #     return self.product.price
#
#     price = get_price.
#
#     def save(self):
#         self.total_price = Decimal(self.quantity)*Decimal(self.price)
#         super().save(*args, **kwargs)
#         self.order.save()
#
#     def increase_quantity(self):
#         self.quantity += 1
#
#     def __str__(self):
#         return self.product, self.quantity
