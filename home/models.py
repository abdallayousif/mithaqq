from random import random
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from metheqq_root.models import Campany
from django.shortcuts import  get_object_or_404
from metheqq_root.models import Marketers

# Create your models here.


class Catogrey(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    sulg = models.SlugField(max_length=255, unique=True)
    campany_id_id = models.ForeignKey(Campany, on_delete=models.CASCADE ,related_name='campany_id')
    

    class Meta:
        verbose_name_plural = 'catogeryes'

    def get_absolute_url(self):
        return reverse("home:catogrey_list", args=[self.sulg])

    def __str__(self):
        return self.name_name


    
class Product(models.Model):
    cat_id_id = models.ForeignKey(Catogrey, on_delete=models.CASCADE, related_name='product1')
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='product_cerateby')
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    comission = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse("home:product_detail", args=[self.slug])

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.product.title




class campany_permision(models.Model):
    campany_id = models.ForeignKey(Campany, on_delete=models.CASCADE)
    marketer_id = models.ForeignKey(Marketers, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.marketer_id)


class catogry_permision(models.Model):
    cat_id = models.ForeignKey(Catogrey, verbose_name=_("id"), on_delete=models.CASCADE)
    marketer_id = models.ForeignKey(Marketers, verbose_name=_("id"), on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return str(self.marketer_id)
