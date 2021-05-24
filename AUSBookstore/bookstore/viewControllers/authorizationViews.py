from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from bookstore.decorators import unauthenticated_user, allowed_users, shopkeeper_only
from bookstore.forms.authenticationForm import CustomerSignUpForm


# Create your views here.

# user login
@unauthenticated_user
def login_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, 'index.html')
    context = {}
    return render(request, 'index.html', context)


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('customer_register')
    else:
        form = CustomerSignUpForm()

    context = {'form': form}
    return render(request, 'customer/register.html', context)


@login_required(login_url='login')
@shopkeeper_only
def shopkeeper_homepage(request):
    return render(request, 'storekeeper/homepage.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def customer_homepage(request):
    return render(request, 'storekeeper/homepage.html')


def logout_user(request):
    logout(request)
    return redirect('login')
