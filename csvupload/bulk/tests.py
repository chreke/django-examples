from django.test import TestCase

from .forms import ProductForm

class ProductFormTest(TestCase):
    def test_valid_productform(self):
        form = ProductForm({
            "name": "ExpensiBike XL1000",
            "sku": "2E50F578",
            "price": 799,
            "description": "A very expensive bike",
        })
        self.assertTrue(form.is_valid())


    def test_invalid_productform(self):
        form = ProductForm({
            "name": "ExpensiBike XL1000",
            "sku": "2E50F578",
            "price": -4,
            "description": "A very expensive bike",
        })
        self.assertFalse(form.is_valid())
