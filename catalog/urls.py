from django.urls import path
from catalog.views import HomeListView, ContactsCreateView, ProductCardView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
        path('', HomeListView.as_view(), name="home"),
        path('contacts/', ContactsCreateView.as_view(), name="contacts"),
        path('<int:pk>/product1/', ProductCardView.as_view(), name="product1")
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
