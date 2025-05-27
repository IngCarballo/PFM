from django.db import models
from accounts.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Movement(models.Model):
    MOVEMENT_TYPES = (
        ('IN', 'Ingreso'),
        ('OUT', 'Egreso'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movement_type = models.CharField(max_length=3, choices=MOVEMENT_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    payment_method = models.CharField(max_length=50)
    link = models.URLField(blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.get_movement_type_display()} - {self.amount}"
