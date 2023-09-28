from django.urls import path
from . import views

urlpatterns = [
    path('/', views.stock_index, name='stock-index'),
    path('/tambah', views.tambah_stock, name='stock-add')
]
