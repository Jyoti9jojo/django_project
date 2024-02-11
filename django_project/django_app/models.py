from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.FloatField(default=10)
    product_image = models.ImageField()
    rating = models.FloatField()
    active = models.BooleanField(default=True)
    available_quantity = models.IntegerField()
    
    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return f"{self.product_name}"