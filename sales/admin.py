from django.contrib import admin

from .models import SalesModel, CustomerModel
# Register your models here.

class SaleAdmin(admin.ModelAdmin):
    list_display = ['order_no','customer','sku','quantity','price','total_price','date']
    search_fields =['order_no','customer__customer','sku__sku']
admin.site.register(SalesModel,SaleAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer','contact']
    search_fields =['customer']

admin.site.register(CustomerModel,CustomerAdmin)