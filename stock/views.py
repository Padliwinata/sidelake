from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db.models import F


from .models import Stock, History, JenisEvent
from datetime import datetime, timedelta
# Create your views here.


def stock_index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    stocks = Stock.objects.filter(is_deleted=False, merchant=request.user.merchant, jumlah__gt=0)
    barang = Stock.objects.all()
    context = {'stocks': stocks, 'barang': barang}
    return render(request, 'stock/index.html', context)


def update_stock(request):
    if request.method == 'GET':
        stocks = Stock.objects.filter(
            is_deleted=False).exclude(jumlah=0)
        barang = Stock.objects.all()
        context = {'stocks': stocks, 'barang': barang}
        return render(request, 'stock/StockUp.html', context)
    elif request.method == 'POST':
        pass


def log_stock(request):
    stocks = History.objects.filter(stock__is_deleted=False, stock__merchant=request.user.merchant, jenis=JenisEvent.KELUAR.value)
    list_barang = Stock.objects.filter(is_deleted=False, merchant=request.user.merchant, jumlah__gt=0)
    context = {'stocks': stocks, 'list_barang': list_barang}
    return render(request, 'stock/StockDown.html', context)


def tambah_stock(request):
    if request.method == 'POST':
        data = request.POST
        namabarang = data.get('nama')
        jumlah = data.get('jumlah')
        res = Stock.objects.filter(stock_id=namabarang).update(jumlah=jumlah)
        res = Stock.objects.get(pk=namabarang)
        report = History(
            stock=res, jenis=JenisEvent.MASUK.value, jumlah=jumlah)
        report.save()

    return redirect('stock-index')


def edit_stock(request, stock_id):
    if request.method == 'POST':
        data = request.POST
        jumlah = data.get('jumlah')
        # input_date = datetime.strptime(expired, '%m/%d/%Y')
        # formatted_date = input_date.strftime('%Y-%m-%d')
        res = Stock.objects.get(pk=stock_id)
        history = History(stock=res, jenis=JenisEvent.EDIT.value, jumlah=jumlah)
        history.save()
        res = Stock.objects.filter(stock_id=stock_id).update(jumlah=jumlah)

        return redirect('stock-index')

    elif request.method == 'GET':
        edit = Stock.objects.get(pk=stock_id)
        stocks = Stock.objects.all()
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

        return redirect('barang-index')

    elif request.method == 'GET':
        edit = Stock.objects.get(pk=stock_id)
        stocks = Stock.objects.all()
        edit.expired = edit.expired.strftime("%Y-%m-%d")
        context = {'data': edit, 'stocks': stocks}
        return render(request, 'stock/EditBarang.html', context)


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
        jumlah = data.get('jumlah')
        satuan = data.get('satuan')
        # expired = data.get('expired')

        input_date = datetime.now()
        res = Stock.objects.filter(last_update__date=input_date.date())
        if len(res) == 0:
            urutan = '01'
        else:
            list_stock_id = [stock.stock_id for stock in res]
            urutan = int(max(list_stock_id, key=lambda x: int(x[-2:]))[-2:])+1
        codebarang = input_date.strftime('%d%m%Y') + str(urutan).zfill(2)
        datasave = Stock(stock_id=codebarang, nama=namabarang,
                         jumlah=jumlah, satuan=satuan, merchant=request.user.merchant)
        datasave.save()
        history = History(stock=datasave, jenis=JenisEvent.MASUK.value, jumlah=jumlah)
        history.save()
        return redirect('stock-index')

def stock_down(request):
    if request.method == 'POST':
        data = request.POST
        jumlah = data.get('jumlah')
        stock_id = data.get('barang')
        res = Stock.objects.get(pk=stock_id)
        stock = int(jumlah)
        history = History(stock=res, jenis=JenisEvent.KELUAR.value, jumlah=stock)
        history.save()
        res = Stock.objects.filter(stock_id=stock_id).update(jumlah=F('jumlah') - jumlah)
        return redirect('stock-log')
    # elif request.method == 'GET':
    #     list_barang = Stock.objects.filter(is_deleted=False, added_by=request.user)
    #     record = History.objects.filter(updated_by=request.user)
    #     print(list_barang)
    #     return render('stock/StockDown.html', context={'list_barang': list_barang, 'record': record})


def history(request):
    histories = History.objects.filter(stock__is_deleted=False, stock__merchant=request.user.merchant)
    return render(request, 'stock/history.html', context={'histories': histories})

def edit_history(request, stock_id):
    if request.method == 'POST':
        data = request.POST
        jumlah = data.get('jumlah')
        # input_date = datetime.strptime(expired, '%m/%d/%Y')
        # formatted_date = input_date.strftime('%Y-%m-%d')
        # res = Stock.objects.get(pk=stock_id)
        # history = History(stock=res, jenis=JenisEvent.EDIT.value, jumlah=jumlah)
        # history.save()
        
        # res = Stock.objects.filter(stock_id=stock_id).update(jumlah=jumlah)
        return redirect('stock-index')
    elif request.method == 'GET':
        edit = History.objects.get(pk=stock_id)
        stocks = Stock.objects.all()
        origin = request.get_full_path()
        context = {'data': edit, 'stocks': stocks, 'origin': origin}
        return render(request, 'stock/Editstory.html', context)        


# def login(request):
#     if request.user.is_authenticated:
#         username = request.user.username
#         return redirect('stock-index', {'username': username})
#     else:
#         return render(request, 'stock/login.html')

# def handle_auth(request):
#     if 
