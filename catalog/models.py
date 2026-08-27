from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    COMPANY_TYPES = [
        ('civil', 'Civil Engineer'),
        ('architect', 'Architect'),
        ('contractor', 'Contractor'),
    ]
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=20, choices=COMPANY_TYPES)
    location = models.CharField(max_length=200)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Plan(models.Model):
    STYLE_CHOICES = [
        ('modern', 'Modern'),
        ('classical', 'Classical'),
        ('minimalist', 'Minimalist'),
        ('industrial', 'Industrial'),
    ]
    title = models.CharField(max_length=200)
    blueprint_image = models.URLField(blank=True)
    area_sqft = models.DecimalField(max_digits=8, decimal_places=2)
    style = models.CharField(max_length=50, choices=STYLE_CHOICES)
    rooms = models.PositiveIntegerField()
    floors = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class InteriorDesign(models.Model):
    ROOM_TYPES = [
        ('living', 'Living Room'),
        ('bedroom', 'Bedroom'),
        ('kitchen', 'Kitchen'),
        ('bathroom', 'Bathroom'),
        ('office', 'Office'),
    ]
    room_type = models.CharField(max_length=50, choices=ROOM_TYPES)
    style = models.CharField(max_length=50)
    images = models.URLField(blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, 
                             null=True, blank=True)
    products_used = models.ManyToManyField(Product, blank=True)

    def __str__(self):
        return f"{self.room_type} - {self.style}"