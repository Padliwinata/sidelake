from django.shortcuts import render, redirect
from django.http import JsonResponse

from .models import Stock, History, JenisEvent
from datetime import datetime, timedelta
# Create your views here.


def stock_index(request):
    stocks = Stock.objects.filter(
        is_deleted=False).exclude(expired__year='1970')
    barang = Stock.objects.all()
    context = {'stocks': stocks, 'barang': barang}
    return render(request, 'stock/index.html', context)


def update_stock(request):
    if request.method == 'GET':
        stocks = Stock.objects.filter(
            is_deleted=False).exclude(expired__year='1970')
        barang = Stock.objects.all()
        context = {'stocks': stocks, 'barang': barang}
        return render(request, 'stock/StockUp.html', context)
    elif request.method == 'POST':
        pass


def log_stock(request):
    stocks = History.objects.all()
    context = {'stocks': stocks}
    return render(request, 'stock/StockDown.html', context)


def tambah_stock(request):
    if request.method == 'POST':
        data = request.POST
        namabarang = data.get('nama')
        jumlah = data.get('jumlah')
        satuan = data.get('satuan')
        expired = data.get('expired')
        input_date = datetime.strptime(expired, '%Y-%m-%d')
        # formatted_date = input_date.strftime('%Y-%m-%d')
        res = Stock.objects.filter(expired=input_date)
        if len(res) == 0:
            urutan = '01'
        else:
            list_stock_id = [stock.stock_id for stock in res]
            urutan = int(max(list_stock_id, key=lambda x: int(x[-2:]))[-2:])+1
        codebarang = input_date.strftime('%d%m%Y') + str(urutan).zfill(2)
        datasave = Stock(stock_id=codebarang, nama=namabarang,
                         jumlah=jumlah, satuan=satuan, expired=input_date)
        datasave.save()

        report = History(
            stock=datasave, jenis=JenisEvent.MASUK.value, jumlah=jumlah)
        report.save()

    return redirect('stock-index')


def edit_stock(request, stock_id):
    if request.method == 'POST':
        data = request.POST
        namabarang = data.get('nama')
        stock = data.get('jumlah')
        satuan = data.get('satuan')
        # input_date = datetime.strptime(expired, '%m/%d/%Y')
        # formatted_date = input_date.strftime('%Y-%m-%d')
        res = Stock.objects.get(pk=stock_id)
        res.nama = namabarang
        prev_jumlah = res.jumlah
        res.jumlah = stock
        res.satuan = satuan
        res.save()
        stock = int(stock)
        if prev_jumlah > stock:
            history = History(
                stock=res, jenis=JenisEvent.KELUAR.value, jumlah=prev_jumlah-stock)
            history.save()
        elif stock > prev_jumlah:
            history = History(
                stock=res, jenis=JenisEvent.MASUK.value, jumlah=stock-prev_jumlah)
            history.save()

        return redirect('stock-index')

    elif request.method == 'GET':
        edit = Stock.objects.get(pk=stock_id)
        stocks = Stock.objects.all()
        edit.expired = edit.expired.strftime("%Y-%m-%d")
        context = {'data': edit, 'stocks': stocks}
        return render(request, 'stock/Editstock.html', context)

def edit_barang(request, stock_id):
    if request.method == 'POST':
        data = request.POST
        namabarang = data.get('nama')
        satuan = data.get('satuan')
        expired = data.get('date')
        # input_date = datetime.strptime(expired, '%m/%d/%Y')
        # formatted_date = input_date.strftime('%Y-%m-%d')
        res = Stock.objects.get(pk=stock_id)
        res.nama = namabarang
        res.satuan = satuan
        res.expired = expired
        res.save()

        return redirect('stock-index')

    elif request.method == 'GET':
        edit = Stock.objects.get(pk=stock_id)
        stocks = Stock.objects.all()
        edit.expired = edit.expired.strftime("%Y-%m-%d")
        context = {'data': edit, 'stocks': stocks}
        return render(request, 'stock/Editstock.html', context)


def delete_stock(request, stock_id):
    if request.method == 'POST':
        Stock.objects.filter(stock_id=stock_id).update(is_deleted=True)
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


def index_barang(request):
    if request.method == 'GET':
        barang = Stock.objects.filter(is_deleted=False)
        context = {'barang': barang}
        return render(request, 'stock/indexBarang.html', context=context)


def save_barang(request):
    if request.method == 'POST':
        data = request.POST
        namabarang = data.get('nama')
        jumlah = 0
        satuan = data.get('satuan')
        expired = data.get('date')

        input_date = datetime.strptime(expired, '%Y-%m-%d')
        res = Stock.objects.filter(expired=input_date)
        if len(res) == 0:
            urutan = '01'
        else:
            list_stock_id = [stock.stock_id for stock in res]
            urutan = int(max(list_stock_id, key=lambda x: int(x[-2:]))[-2:])+1
        codebarang = input_date.strftime('%d%m%Y') + str(urutan).zfill(2)
        datasave = Stock(stock_id=codebarang, nama=namabarang,
                         jumlah=jumlah, satuan=satuan, expired=input_date)
        datasave.save()
        return redirect('barang-index')

    # elif request.method == 'POST':
