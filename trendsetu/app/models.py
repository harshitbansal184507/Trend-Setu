from django.db import models
from django.utils import timezone

# Create your models here.
class ClothingProduct(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
    ]
    
    CATEGORY_CHOICES = [
        ('T', 'T-Shirts'),
        ('D', 'Dresses'),
        ('J', 'Jeans'),
        ('S', 'Shirts'),
        ('O', 'Others')
    ]
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    color = models.CharField(max_length=50)  # Added color field
    image = models.ImageField(upload_to='products/')  # Added image field for product images
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for creation

    def __str__(self):
        return self.title
    
    
    
class Bag(models.Model):
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100)  # You might want to use a choices field
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='bags/') 
    created_at = models.DateTimeField(default=timezone.now) 
    # Ensure you have Pillow installed for image handling

    def __str__(self):
        return self.title
    
    
class Accessory(models.Model):
    title = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.CharField(max_length=100)  # e.g., 'Jewelry', 'Belt', etc.
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to='accessories/')
    created_at = models.DateTimeField(default=timezone.now)  # Track creation date

    def __str__(self):
        return self.title    
    
