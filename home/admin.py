from django.contrib import admin
from django.db import models
from .models import (Catogrey, Product, campany_permision, catogry_permision,ProductImage)


# Register your models here.


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'price', 'in_stock', 'is_active', 'create_by']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'in_stock']
    inlines = [ProductImageAdmin]

    class Meta:
        model = Product
        
admin.site.register(campany_permision)
admin.site.register(catogry_permision)


@admin.register(Catogrey)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'sulg']
    prepopulated_fields = {'sulg': ('name',)}
   