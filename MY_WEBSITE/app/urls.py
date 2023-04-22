from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('home', views.home, name='home'),
    path('biography', views.biography, name='biography'),
    path('gallery', views.gallery, name='gallery'),
    path('gallery/<str:section>', views.gallery_section),
    path('exhibitions', views.exhibitions, name='exhibitions'),
    path('publications', views.publications, name='publications'),
    path('prints', views.prints, name='prints'),
    path('contact', views.contact, name='contact'),
    path('cart', views.cart, name='cart'),
    path('send_contact_request', views.send_contact_request, name='send_contact_request'),
    path('send_order_request', views.send_order_request, name='send_order_request'),
]
