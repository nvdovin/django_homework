from .models import Category
from django.core.cache import cache

def get_categories_queryset(key):
    """Вот мой сервисный слой, если его можно так назвать, конечно.
    Эта функция тянется в файлик с формами приложения каталог. Так что если нужно найти его, то он там"""
    
    queryset_cache = cache.get(key)
    if queryset_cache is None:
        queryset = Category.objects.all()
        queryset_cache = cache.set(key, queryset)
    return queryset_cache