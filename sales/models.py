from django.db import models

from inventory.models import InventoryModel
# Create your models here.

class CustomerModel(models.Model):
    customer = models.CharField(max_length=100,verbose_name='Khách hàng')
    contact = models.IntegerField(verbose_name='Liên hệ')

    def __str__(self):
        return self.customer

    class Meta:
        verbose_name_plural = 'Khách hàng'

class SalesModel(models.Model):
    order_no = models.IntegerField(primary_key=True,verbose_name='Mã')
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE,verbose_name='Khách hàng')
    sku = models.ForeignKey(InventoryModel, on_delete=models.CASCADE,verbose_name='Sản phẩm')
    quantity = models.IntegerField(verbose_name='Số lượng')
    price = models.IntegerField(verbose_name='Giá')
    total_price = models.IntegerField(verbose_name='Tổng giá')
    date = models.DateTimeField(auto_now=True,verbose_name='Ngày')

    # def __str__(self):
    #     return self.customer

    class Meta:
        verbose_name_plural = 'Đơn hàng'