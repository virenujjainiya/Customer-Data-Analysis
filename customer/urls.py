
from django.urls import path

from .views import customer_view,customer_regi



urlpatterns = [
    path('',customer_view,name='customer'),
    path('addcustomer/',customer_regi,name='customer_register'),

]
