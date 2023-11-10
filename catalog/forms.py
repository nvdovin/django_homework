from typing import Any
from django import forms as f
from catalog.models import Product


class CreateProduct(f.ModelForm):
    class Meta:
        model = Product
        exclude = ("last_change_date", )
    
    def clean_title(self):
        stop_words_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data.get('title')
        if cleaned_data.lower() in stop_words_list:
            raise f.ValidationError(f'"{cleaned_data}" Недопустимое название для продукта')
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'row'
