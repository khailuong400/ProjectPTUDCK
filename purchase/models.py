from django.db import models

from supplier.models import SupplierModel
from inventory.models import InventoryModel
# Create your models here.

class NewStockModel(models.Model):
    order_no = models.IntegerField(primary_key=True,verbose_name='Mã')
    sku = models.ForeignKey(InventoryModel, on_delete=models.CASCADE,verbose_name='Sản phẩm')
    supplier = models.ForeignKey(SupplierModel, on_delete=models.CASCADE,verbose_name='Nhà cung cấp')
    quantity = models.IntegerField(verbose_name='Số lượng')
    price = models.IntegerField(verbose_name='Giá')
    total_price = models.IntegerField(verbose_name='Tổng giá')
    date = models.DateTimeField(auto_now=True,verbose_name='Ngày')

    def __str__(self):
        return self.sku.sku
    
    class Meta:
        verbose_name_plural = 'Nhập kho'