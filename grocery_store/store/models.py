from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=10)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    

    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    customer_name = models.CharField(max_length=255)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Order #{self.id} by {self.customer_name}"

    def calculate_total(self):
        total = sum(item.subtotal for item in self.orderdetail_set.all())
        self.total_amount = total
        self.save()
        

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.product.price_per_unit
        super().save(*args, **kwargs)
        self.order.calculate_total()
        
        
class Contact(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default="")
    email = models.EmailField(null=False, blank=False, default="")
    subject = models.CharField(max_length=150, null=True, blank=True, default="")
    message = models.CharField(max_length=200, null=False, blank=False, default="")
    