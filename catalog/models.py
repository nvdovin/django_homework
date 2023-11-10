from django.db import models

NULLABLE = {
    "null": True,
    "blank": True
}


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=20, verbose_name="Наименование", unique=True)
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="catalog/media/", **NULLABLE, verbose_name="Изображние")
    category = models.CharField(max_length=20, verbose_name="Категория", **NULLABLE)
    price = models.FloatField(verbose_name="Цена за товар", **NULLABLE)
    creations_date = models.DateField(verbose_name="Дата создания", **NULLABLE)
    last_change_date = models.DateField(**NULLABLE, verbose_name="Дата последнего изменения")
    version_of_product = models.ForeignKey(to='Version', to_field="version_number", blank=True, null=True, on_delete=models.SET_NULL)

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


class Version(models.Model):
    product_name = models.ForeignKey(to='Product', to_field='title', on_delete=models.CASCADE)
    version_number = models.FloatField(unique=True, verbose_name="Номер версии")
    version_title = models.CharField(max_length=100, verbose_name="Название версии")
    is_active_version = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
    
    def __str__(self) -> str:
        if self.is_active_version is True:
            is_activated = "Активная версия"
        else:
            is_activated = "Не активная версия"

        return f'"{self.product_name}" - {self.version_number} - "{is_activated}"'

