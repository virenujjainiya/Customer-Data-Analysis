from os import name
from django.urls import path
from .views import Chart_select,add_purchase,sales_dist_views
urlpatterns = [
    path('',Chart_select,name='home-page'),
    path('add/',add_purchase,name='add'),
    path('sales/',sales_dist_views,name='sales'),

]
