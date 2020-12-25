from django.contrib import admin

# user: imran1 and pass: 123
from .models import Customer,Product,Order,Tag

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)