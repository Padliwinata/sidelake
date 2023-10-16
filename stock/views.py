from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Stock
from datetime import datetime, timedelta
# Create your views here.
def stock_index(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
    return render(request, 'stock/index.html', context)

def update_stock(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
    return render(request, 'stock/StockUp.html',context)

def log_stock(request):
    stocks = Stock.objects.all()
    context = {'stocks': stocks}
    return render(request, 'stock/StockDown.html',context)

def tambah_stock(request):
    if request.method == 'POST' :
        data = request.POST
        namabarang = data.get('nama')
        stock = data.get('jumlah')
        satuan = data.get('satuan')
        expired = data.get('expired')
        input_date = datetime.strptime(expired, '%m/%d/%Y')
        formatted_date = input_date.strftime('%Y-%m-%d')
        res = Stock.objects.filter(expired=formatted_date)
        if len(res) == 0 :
            urutan = '01'
        else :
            list_stock_id = [stock.stock_id for stock in res]
            urutan  =int(max(list_stock_id,key=lambda x : int(x[-2:]))[-2:])+1
        codebarang = input_date.strftime('%d%m%Y') + str(urutan).zfill(2)
        datasave = Stock(stock_id=codebarang, nama=namabarang, jumlah=stock, satuan=satuan, expired=formatted_date)
        datasave.save()

    return redirect('stock-index')

def edit_stock(request, stock_id):
     if request.method == 'POST' :
        data = request.POST
        namabarang = data.get('nama')
        stock = data.get('jumlah')
        satuan = data.get('satuan')
        expired = data.get('date')
        # input_date = datetime.strptime(expired, '%m/%d/%Y')
        # formatted_date = input_date.strftime('%Y-%m-%d')
        res = Stock.objects.get(pk = stock_id)
        res.nama = namabarang
        res.jumlah = stock
        res.satuan = satuan
        res.expired = expired
        res.save()
        return redirect('stock-index')
     
     elif request.method == 'GET' :
        edit = Stock.objects.get(pk = stock_id)
        stocks = Stock.objects.all()
        edit.expired = edit.expired.strftime("%Y-%m-%d")
        context = {'data': edit, 'stocks': stocks}
        return render(request, 'stock/Editstock.html', context)
     

def delete_stock(request,stock_id):
    if request.method == 'GET' :
        Stock.objects.filter(stock_id=stock_id).delete()
        return redirect('stock-index')

def get_stock_data(request, stock_id):
    stock = Stock.objects.get(pk=stock_id)
    data = {
        'stock_id': stock_id,
        'barang': stock.nama,
        'jumlah': stock.jumlah,
    }
    return JsonResponse(data)

def stock_update(request, stock_id):
    if request.method == 'GET':
        stock = Stock.objects.get(pk=stock_id)
        context = {'data': stock}
        return render(request, 'stock/Editstock.html', context)
    # elif request.method == 'POST':

    
