from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True,)
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)],)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products',)
    price = models.FloatField(validators=[MinValueValidator(0.0)],)
    material = models.ManyToManyField(to='Material', through='ProductMaterial', related_name='materials',)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='materials')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.product.name} : {self.material.name}'


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True,)

    def __str__(self):
        return self.name.title()

