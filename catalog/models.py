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