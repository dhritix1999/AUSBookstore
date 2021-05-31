from django.forms import ModelForm
from bookstore.models import Category,Product, Order

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderStatusForm(ModelForm):
    class Meta:
        model = Order
        fields = ['status']