from django import forms as f
from catalog.models import Product


class CreateProduct(f.ModelForm):
    class Meta:
        model = Product
        exclude = ("last_change_date", )