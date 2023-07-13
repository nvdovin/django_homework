from django.core.management import BaseCommand
from catalog.models import Product, Category
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        products_list = [
            {
                "title": "Сосиски",
                "description": "Еда настоящих мужчин",
                "category": "Мясопродукты",
                "price": 150,
                "creations_date": f"{datetime.now().strftime('%Y-%m-%d')}"
            },
            {
                "title": "Колбасы",
                "description": "Еда настоящих детей",
                "category": "Мясопродукты",
                "price": 300,
                "creations_date": f"{datetime.now().strftime('%Y-%m-%d')}"
            },
            {
                "title": "Курица",
                "description": "Еда настоящих женщин",
                "category": "Мясопродукты",
                "price": 450,
                "creations_date": f"{datetime.now().strftime('%Y-%m-%d')}"
            }
        ]

        creating_products = []
        for product_item in products_list:
            creating_products.append(Product(**product_item))
        Product.objects.bulk_create(creating_products)

        category_list = [
            {
                "title": "Еда",
                "description": "Еда для тех, кто любит есть"
            },
            {
                "title": "Напитки",
                "description": "Напитки для тех, кто любит пить"
            },
            {
                "title": "Не знаю, что?",
                "description": "Что это вообще?!"
            }
        ]

        creating_category = []
        for category_item in category_list:
            creating_category.append(Category(**category_item))

        Category.objects.bulk_create(creating_category)
