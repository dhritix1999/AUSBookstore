from django.urls import path
from .viewControllers import authorizationViews, shopkeeperViews

urlpatterns = [

    # authentication
    path('', authorizationViews.login_request, name='login'),
    path('customer/register/', authorizationViews.register, name='customer_register'),
    path('customer/home/', authorizationViews.shopkeeper_homepage, name='customer_home'),
    path('homepage/', authorizationViews.shopkeeper_homepage, name='home'),
    path('logout/', authorizationViews.logout_user, name='logout'),

    #admin stuff
    #category
    path('category/', shopkeeperViews.category_list, name='category_list'),
    path('category/create', shopkeeperViews.create_category, name='create_category'),
    path('category/<int:pk>/update/', shopkeeperViews.update_category, name='update_category'),
    path('category/<int:pk>/delete/', shopkeeperViews.delete_category, name='delete_category'),

    # product
    path('product/', shopkeeperViews.product_list, name='product_list'),
    path('product/create', shopkeeperViews.create_product, name='create_product'),
    path('product/<int:pk>/update', shopkeeperViews.update_product, name='update_product'),

    #view orders
    path('order/', shopkeeperViews.order_list, name='order_list'),



]
