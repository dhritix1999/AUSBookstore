from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from bookstore.models import Category
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from bookstore.form import CustomerSignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


# Create your views here.

# user login
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
    context = {}
    return render(request, 'index.html', context)


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


class customer_register(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'customer/register.html'

    def validation(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def homepage(request):
    return render(request, 'storekeeper/homepage.html')



def logout_view(request):
    logout(request)
    return redirect('/')
