from django.contrib import admin
from stock.models import Stock, History

# Register your models here.
admin.site.register(Stock) 
admin.site.register(History)
