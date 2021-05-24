from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from bookstore.models import Category, Product

from bookstore.decorators import allowed_users, shopkeeper_only
from bookstore.forms.productsForm import OrderForm

# Create your views here.

@login_required(login_url='login')
@allowed_users(allowed_roles=['shopkeeper'])
def category_list(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'storekeeper/category/category-table.html', context)

def create_category(request):
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()

            messages.info(request, 'Category is added successfully')
            return redirect('create_category')
    context = {
        'form': form,
        'update_category': False
    }

    return render(request, 'storekeeper/category/category_form.html', context)


def update_category(request, pk):

    category = Category.objects.get(id=pk)
    form = OrderForm(instance = category)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=category)
        if form.is_valid():
            form.save()

            messages.info(request, 'Category is updated successfully')
            return redirect('create_category')
    context = {
        'form': form,
        'update_category': True
    }

    return render(request, 'storekeeper/category/category_form.html', context)


def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return redirect('category_list')



def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, 'storekeeper/product/product-table.html', context)

def create_product(request):
    return render(request, 'storekeeper/product/product_form.html')


#orders
def order_list(request):
    return None


def update_product(request):
    return None


def delete_product(request):
    return None