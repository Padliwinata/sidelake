from django.urls import path
from . import views

urlpatterns = [
    path('/', views.stock_index, name='stock-index'),
    path('/stockup', views.update_stock, name='stock-update'),
    path('/stocklog', views.log_stock, name='stock-log'),
    path('/tambah', views.tambah_stock, name='stock-tambah'),
    path('/data/<int:stock_id>', views.get_stock_data, name='stock-data'),
    path('/edit/<str:stock_id>', views.edit_stock, name='stock-edit'),
    path('/delete/<str:stock_id>', views.delete_stock, name='stock-delete'),
]
