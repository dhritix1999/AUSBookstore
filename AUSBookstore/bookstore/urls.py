from django.urls import path
from .viewControllers import authorizationViews

urlpatterns = [

    # authentication
    path('', authorizationViews.login_request, name='login'),
    path('customer/register', authorizationViews.register, name='customer_register'),
    path('logout/', authorizationViews.logout_view, name='logout'),

    path('homepage/', authorizationViews.homepage, name='home'),

]
