from django.db import models


class Stock(models.Model):
    """docstring for Stock."""
    category = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        """Return string representation of the Stock object"""

        return self.category


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        """Return string representation of the Tag object"""

        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=255, null=True)
    price = models.FloatField(null=True)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    code = models.CharField(max_length=100, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    image = models.ImageField(
        upload_to='products',
        default="default.png", null=True, blank=True
    )
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        """Return string representation of the Product object"""

        return self.name
