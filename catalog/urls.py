from django.urls import path
from catalog.views import home, contacts, product1
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
        path('', home, name="home"),
        path('contacts/', contacts, name="contacts"),
        path('product1/', product1, name="product1")
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
