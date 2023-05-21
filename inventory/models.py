from django.db import models

# Create your models here.

class InventoryModel(models.Model):
    sku = models.CharField(max_length=100,verbose_name='Sản phẩm')
    available_quantity = models.IntegerField(verbose_name='Hiện còn')
    
    def __str__(self):
        return self.sku
    
    class Meta:
        verbose_name_plural = 'Kho'
