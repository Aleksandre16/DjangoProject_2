from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    page_count = models.IntegerField()
    category = models.CharField(max_length=200)
    image = models.ImageField(default=None, null=True, blank=True)

    def __str__(self):
        return self.name
