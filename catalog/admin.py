from django.contrib import admin
from .models import Category, Company, Product, Plan, InteriorDesign

admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Product)
admin.site.register(Plan)
admin.site.register(InteriorDesign)