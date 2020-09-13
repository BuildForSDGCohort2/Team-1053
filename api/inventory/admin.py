from django.contrib import admin
from .models import Stock, Tag, Product

admin.site.register(Stock)
admin.site.register(Tag)
admin.site.register(Product)
