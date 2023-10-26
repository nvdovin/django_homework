from django.db import models

NULLABLE = {
    "null": True,
    "blank": True
}


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=20, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="catalog/media/", **NULLABLE, verbose_name="Изображние")
    category = models.CharField(max_length=20, verbose_name="Категория", **NULLABLE)
    price = models.FloatField(verbose_name="Цена за товар", **NULLABLE)
    creations_date = models.DateField(verbose_name="Дата создания", **NULLABLE)
    last_change_date = models.DateField(**NULLABLE, verbose_name="Дата последнего изменения")

    def __str__(self):
        return f"{self.title} {self.category} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Category(models.Model):
    title = models.CharField(max_length=20, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
