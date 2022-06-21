from django.forms import FileField, Form, ModelForm

from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "sku", "price", "description"]


class ImportForm(Form):
    products_file = FileField()
