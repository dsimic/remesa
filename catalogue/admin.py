from django.contrib import admin

# Register your models here.
from catalogue.models import Catalogue, CatalogueCategory, Product,\
    FeaturedProduct


admin.site.register(Catalogue)
admin.site.register(CatalogueCategory)
admin.site.register(Product)
admin.site.register(FeaturedProduct)
