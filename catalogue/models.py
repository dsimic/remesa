from django.db import models

import datetime as dt

# Create your models here.


class Catalogue(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    publisher = models.CharField(max_length=300)
    description = models.TextField()
    pub_date = models.DateTimeField(default=dt.datetime.now)

    def __unicode__(self):
        return self.name


class CatalogueCategory(models.Model):
    catalogue = models.ForeignKey('Catalogue', related_name='categories')
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='children')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('CatalogueCategory', related_name='products')
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=150)
    description = models.TextField()
    photo = models.ImageField(upload_to='media/product_photo', blank=True)
    manufacturer = models.CharField(max_length=300, blank=True)
    price_in_cop = models.DecimalField(max_digits=6, decimal_places=3)

    def __unicode__(self):
        return str(self.category) + ' - ' + self.name


class FeaturedProduct(models.Model):
    product = models.ForeignKey('Product', related_name='featured_products')

    def __unicode__(self):
        return str(self.product)
