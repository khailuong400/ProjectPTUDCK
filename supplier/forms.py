from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Button

from .models import SupplierModel


class SupplierForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Lưu', css_class='mt-2 btn btn-dark'))
        self.helper.add_input(Button('cancel', 'Hủy', onclick="location.href = '/supplier/suppliers-list/'", css_class='ms-3 mt-2 btn btn-dark'))
        self.helper.layout = Layout(
            Row(
                Column('name', css_class='mt-4'),
                Column('contact', css_class='mt-4'),
                Column('email', css_class='mt-4'),
                Column('address', css_class='mt-4'),
            )
        )

    class Meta:
        model = SupplierModel
        fields = '__all__'
        labels = {
            'name': 'Tên nhà cung cấp',
            'contact': 'Liên hệ',
            'email': 'Email',
            'address': 'Địa chỉ' 
            }


class SupplierEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Lưu', css_class='mt-2 btn btn-dark'))
        self.helper.add_input(Button('cancel', 'Hủy', onclick="location.href = '/supplier/suppliers-list/'", css_class='ms-3 mt-2 btn btn-dark'))
        self.helper.layout = Layout(
            Row(
                Column('contact', css_class='mt-4'),
                Column('email', css_class='mt-4'),
                Column('address', css_class='mt-4'),
            )
        )

    class Meta:
        model = SupplierModel
        exclude = ['name']
        labels = {
            'contact': 'Liên hệ',
            'email': 'Email',
            'address': 'Địa chỉ' 
            }