from django.contrib import admin
from .models import Brand, Model, Car

# Register your models here.

class BrandAdmin(admin.ModelAdmin):
    pass 
    
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(Car)