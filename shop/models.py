from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/Product/")
    desc = models.TextField()
    price = models.IntegerField()
    discount = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    delivery_address = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

