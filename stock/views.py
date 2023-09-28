from django.shortcuts import render
from .models import Stock

# Create your views here.
def stock_index(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
    return render(request, 'stock/index.html', context)

def tambah_stock(request):
    return render(request, 'stock/StockUp.html')
