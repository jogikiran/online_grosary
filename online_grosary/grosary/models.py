from django.db import models
from users.models import User


class Grosary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grosary_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_picture')
    prize = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    ORDER_STATUS_CHOISE = [
        ('order confirmed', 'Order Confirmed'),
        ('order processing', 'Order Processing'),
        ('order shipping', 'Order Shipping'),
        ('order cancelled', 'Order Cancelled'),
        ('order delivered', 'Order Delivered'),
    ]
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    grosary = models.ForeignKey(Grosary, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=ORDER_STATUS_CHOISE, default='order confirmed')
    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
