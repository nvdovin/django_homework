from django.contrib import admin
from catalog.models import Product, Category, Version

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "category")
    list_filter = ["category"]
    search_fields = ("title", "description")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("product_name", "version_number", "version_title", "is_active_version")
