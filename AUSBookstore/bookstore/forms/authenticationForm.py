from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from bookstore.models import Customer, Storekeeper, User
from django import forms
from django.contrib.auth.models import Group

COLLEGE_CHOICES = [
    ('CEN', 'CEN'),
    ('CAAD', 'CAAD'),
    ('CAS','CAS'),
    ('SBA', 'SBA'),
    ('none', 'None')
]

TYPE_CHOICES = [
    ('student', 'Student'),
    ('faculty', 'Faculty'),
    ('staff', 'Staff'),
]

DEPARTMENT_CHOICES = [
    ('chemical engineering', 'Chemical Engineering'),
    ('civil engineering', 'Civil Engineering'),
    ('computer science and engineering', 'Computer Science and Engineering'),
    ('electrical engineering', 'Electrical Engineering'),
    ('architecture', 'Architecture'),
    ('art and design', 'Art and Design'),
    ('economics', 'Economics'),
    ('finance', 'Finance'),
    ('international studies', 'International Studies'),
    ('english', 'English'),
]


class CustomerSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    type = forms.CharField(label='Type', widget=forms.Select(choices=TYPE_CHOICES), required=True)
    college = forms.CharField(label='College', widget=forms.Select(choices=COLLEGE_CHOICES), required=True)
    department = forms.CharField(label='Department', widget=forms.Select(choices=DEPARTMENT_CHOICES), required=True)
    phone_number = forms.CharField(required=True)
    location_lat = forms.FloatField(required=True)
    location_lng = forms.FloatField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)

        user.is_customer = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')

        user.save()

        customer = Customer.objects.create(user=user)
        customer.type = self.cleaned_data.get('type')
        customer.college = self.cleaned_data.get('college')
        customer.department = self.cleaned_data.get('department')
        customer.phone_number = self.cleaned_data.get('phone_number')
        customer.location_lat = self.cleaned_data.get('location_lat')
        customer.location_lng = self.cleaned_data.get('location_lng')

        customer.save()

        user_group = Group.objects.get(name='customer')
        user_group.user_set.add(user)
        return customer


class StorekeeperSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)

        user.is_shopkeeper = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()

        storekeeper = Storekeeper.objects.create(user=user)
        storekeeper.save()
        return storekeeper
