from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        fruits = Category.objects.create(title='фрукты')

        Product.objects.create(title='банан', description='', price='146', category=fruits, image="/Банан.png")






