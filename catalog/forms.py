from typing import Any
from django import forms as f
from catalog.models import Category, Product, Version


class CreateProduct(f.ModelForm):
    title = f.CharField(label='Наименование', max_length=200, widget=f.TextInput(attrs={'class': 'my-same-widht'}))
    description = f.CharField(label='Описание', widget=f.Textarea(attrs={'class': 'my-same-widht my-same-height'}))
    image = f.ImageField(label='Изображние', required=False, widget=f.FileInput(attrs={'class': 'my-same-widht'}))
    category = f.ModelChoiceField(label='Категория', 
                                    required=False, 
                                    widget=f.Select(attrs={'class': 'my-same-widht'}),
                                    queryset=Category.objects.all()
                                    )
    price = f.FloatField(label='Цена за товар', required=False, widget=f.NumberInput(attrs={'class': 'my-same-widht'}))
    version_of_product = f.ModelChoiceField(label='Версия', queryset=Version.objects.all(),
                                            required=False, widget=f.Select(attrs={'class': 'my-same-widht'}))

    class Meta:
        model = Product
        exclude = ("last_change_date", "creations_date", "author", "is_published")
    
    def clean_title(self):
        stop_words_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data.get('title')
        if cleaned_data.lower() in stop_words_list:
            raise f.ValidationError(f'"{cleaned_data}" Недопустимое название для продукта')
        return cleaned_data


class ModeratorUpdateProduct(f.ModelForm):
    description = f.CharField(label='Описание', widget=f.Textarea(attrs={'class': 'my-same-widht my-same-height'}))
    category = f.ModelChoiceField(label='Категория', 
                                    required=False, 
                                    widget=f.Select(attrs={'class': 'my-same-widht'}),
                                    queryset=Category.objects.all()
                                    )

    class Meta:
        model = Product
        fields = ('description', 'category')

