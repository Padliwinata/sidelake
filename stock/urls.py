from django.urls import path
from . import views

urlpatterns = [
    path('/', views.stock_index, name='stock-index'),
    path('/stockup', views.update_stock, name='stock-update'),
    path('/stocklog', views.log_stock, name='stock-log'),
    path('/tambah', views.tambah_stock, name='stock-tambah'),
    # path('/data/<int:stock_id>', views.get_stock_data, name='stock-data'),
    path('/edit/<str:stock_id>', views.edit_stock, name='stock-edit'),
    path('/editBarang/<str:stock_id>', views.edit_barang, name='barang-edit'),
    # path('/update/<str:stock_id>', views.update_stock, name='stock-update'),
    path('delete/<str:stock_id>', views.delete_stock, name='stock-delete'),
    path('/inventory', views.index_barang, name='barang-index'),
    path('/inventory/save', views.save_barang, name='barang-simpan'),
    path('/stockdown', views.stock_down, name='stock-down'),
    # path('/login', views.login, name='login')
]
