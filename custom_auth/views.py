from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        username = request.user.username
        return redirect('stock-index', {'username': username})
    else:
        return render(request, 'stock/login.html')

def handle_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in now as {username}")
                return redirect('stock-index', {'username': username})
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
