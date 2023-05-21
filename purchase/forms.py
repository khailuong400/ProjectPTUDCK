from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Button

from .models import NewStockModel


class NewStockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_method = 'POST'
            self.helper.form_action = ''
            self.helper.add_input(Submit('submit', 'Lưu', css_class='mt-2 btn btn-dark'))
            self.helper.add_input(Button('cancel', 'Hủy', onclick="location.href = '/purchase/purchase-history/'", css_class='ms-3 mt-2 btn btn-dark'))
            self.helper.layout = Layout(
                Row(
                    Column('sku', css_class='mt-4'),
                    Column('supplier', css_class='mt-4'),
                    Column('quantity', css_class='mt-4'),
                    Column('price', css_class='mt-4'),
                )
            )

    class Meta:
        model = NewStockModel
        exclude = ['order_no', 'date', 'total_price']
        labels = {
            'sku': 'Sản phẩm',
            'supplier': 'Nhà cung cấp',
            'quantity': 'Số lượng',
            'price': 'Giá mỗi số lượng (Rs.)' 
            }
