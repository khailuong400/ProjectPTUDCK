from django.contrib import admin
from .models import InventoryModel
# Register your models here.

class InventoryAdmin(admin.ModelAdmin):
    list_display = ['sku','available_quantity']
    search_fields = ['sku']
admin.site.register(InventoryModel,InventoryAdmin)
