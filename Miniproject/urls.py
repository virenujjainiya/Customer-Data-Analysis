"""Miniproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include
from Miniproject.view import (card1_view,card2_view,card3_view, card4_view, card5_view, card6_view, home_view,registerview,loginview,logoutview)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='homepage'),
    path('card1/',card1_view,name='card1'),
    path('card2/',card2_view,name='card2'),
    path('card3/',card3_view,name='card3'),
    path('card4/',card4_view,name='card4'),
    path('card5/',card5_view,name='card5'),
    path('card6/',card6_view,name='card6'),


    path('register/',registerview,name='register'),
    path('login/',loginview.as_view(),name='login'),
    path('logout/',logoutview.as_view(),name='logout'),
    path('performance/',include('product.urls'),name='product'),
    path('upload/',include('read_csv.urls'),name='csvs'),
    path('customer/',include('customer.urls'),name='customer')

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT) 