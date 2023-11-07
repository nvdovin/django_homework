from django.urls import path
from catalog import views as v
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
        path('', v.HomeListView.as_view(), name="home"),
        path('contacts/', v.ContactsCreateView.as_view(), name="contacts"),
        path('<int:pk>/product1/', v.ProductCardView.as_view(), name="product1"),
        path('create_product/', v.ProductCreateView.as_view(), name="create_product")
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
