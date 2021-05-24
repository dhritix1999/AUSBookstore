from django.forms import ModelForm
from bookstore.models import Category,Product

class OrderForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'