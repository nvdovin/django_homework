from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        fruits = Category.objects.create(title='фрукты')
        vegetables = Category.objects.create(title='овощи')
        berry = Category.objects.create(title='ягоды')
        meet = Category.objects.create(title='мясо')
        fish = Category.objects.create(title='рыба')

        Product.objects.create(title='банан', description='', price='146', category=fruits, image="/Банан.png")
        Product.objects.create(title='помидор', description='', price='120', category=vegetables, image='/Помидор.png')
        Product.objects.create(title='орех', description='', price='250', category=berry, image='/Орех.png')
        Product.objects.create(title='баранина', description='', price='600', category=meet, image='/Баранина.png')
        Product.objects.create(title='курица', description='', price='350', category=meet, image='/Курица.png')
        Product.objects.create(title='килька', description='', price='700', category=fish, image='/Рыба.png')
        Product.objects.create(title='черешня', description='', price='430', category=berry, image='/Черешня.png')
        Product.objects.create(title='клубника', description='', price='380', category=berry, image='/Клубника.png')






