from django.contrib import admin

from .models import SupplierModel

# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name','contact','email','address']
    search_fields = ['name','email','address']
admin.site.register(SupplierModel,SupplierAdmin)