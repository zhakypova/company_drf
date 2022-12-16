from django.db import models

class Firm(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    items = models.ManyToManyField(Firm, through='Item')

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




