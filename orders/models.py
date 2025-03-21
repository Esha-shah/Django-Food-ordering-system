import os
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
# def food_image_upload_path(instance, filename):
#     """Generate file path as id_name.extension"""
#     extension = filename.split('.')[-1]  # Get file extension (jpg, png, etc.)
#     new_filename = f"{instance.pk}_{instance.name}.{extension}"
#     print
#     return os.path.join("food_item_pics/", new_filename)

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to="food_item_pics/", null=True, blank=True,default="food_item_pics/food_default.png")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_vegan = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'category', 'is_vegan', 'is_vegetarian'], 
                name='unique_food_item'
            )
        ]
    
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.quantity * self.food_item.price

    def __str__(self):
        return f"{self.food_item.name} - {self.quantity}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Completed', 'Completed'),('Cancelled', 'Cancelled')], default='Pending')

    def __str__(self):
        return f"Order {self.id} - {self.user.username}"
    

class OrderHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order {self.order.id}: {self.quantity} x {self.item.name}"
    


