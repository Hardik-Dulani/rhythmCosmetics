"""rhythmCosmetics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('accounts/',include('allauth.urls')),
    path('checkout/',views.checkout,name='checkout'),
    path('logout', views.handelLogout, name="handleLogout"),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name="Search"),
    path('products/<int:myid>',views.productview,name="ProductView"),
    path('search/products/<int:myid>',views.productview,name="ProductView"),
    path('cart/',views.cart_view,name='cartView'),
    path('orders/',views.orders,name='myorders'),
    path('about/',views.about,name="about"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
