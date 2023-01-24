from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("search/", views.Search.as_view(), name='search'),
    path('itemadd/', views.item_add, name='itemadd'),
    path('ad-car/<int:pk>/', views.ad_detail_car, name='ad_detail_car'),
    path('ad-scooters/<int:pk>/', views.ad_detail_scooters, name='ad_detail_scooters'),
    path('ad-motocycles/<int:pk>/', views.ad_detail_motorcycles, name='ad_detail_motorcycles')
]
