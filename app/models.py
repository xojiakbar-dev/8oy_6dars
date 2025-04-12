from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Food(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category , on_delete=models.SET_NULL , null=True)
    price = models.DecimalField(max_digits=20 , decimal_places=2)
    discount = models.DecimalField(max_digits=10 , decimal_places=2)

    def __str__(self):
        return f"{self.price} narxdagi {self.name} chegirmada {self.price - self.discount} so'm"



class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Food , on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} tomonidan {self.product.name} ga sharh yozildi"
