from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        username = request.user.username
        return redirect('stock-index', {'username': username})
    else:
        return render(request, 'stock/login.html')

def handle_login(request):
    pass
