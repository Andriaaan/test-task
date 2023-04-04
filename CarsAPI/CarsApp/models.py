from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=50)
    headquarters_country = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"
    
    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=50)
    year_of_issue = models.PositiveIntegerField()
    body_style = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Models"
    
    def __str__(self):
        return f"{self.name} {self.year_of_issue}, {self.body_style}"

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.PositiveIntegerField()
    exterior_color = models.CharField(max_length=50)
    interior_color = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    engine = models.CharField(max_length=50)
    is_on_sale = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
    
    def __str__(self):
        return f"{self.brand.name} {self.model.name} {self.model.year_of_issue}"