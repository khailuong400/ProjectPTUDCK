from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Button

from .models import InventoryModel


class InventoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Lưu', css_class='mt-2 btn btn-dark'))
        self.helper.add_input(Button('cancel', 'Hủy', onclick="location.href = '/index/'", css_class='ms-3 mt-2 btn btn-dark'))
        self.helper.layout = Layout(
            Row(
                Column('sku', css_class='mt-4'),
                Column('available_quantity', css_class='mt-4'),            )
        )

    class Meta:
        model = InventoryModel
        fields = '__all__'
        labels = {
            'sku': 'Sản phẩm',
            'available_quantity': 'Số lượng',
            }
            