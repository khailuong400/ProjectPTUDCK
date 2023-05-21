from django.contrib import admin

from .models import NewStockModel
# Register your models here.

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ['order_no','sku','supplier','quantity','price','total_price','date']
    search_fields = ['order_no','sku__sku','supplier__name']
admin.site.register(NewStockModel,PurchaseAdmin)