from django.contrib import admin
from .models import User, Customer, Storekeeper, Product, Category, Order, OrderItem
# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Storekeeper)

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)

