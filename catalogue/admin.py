from django.contrib import admin

# Register your models here.
from catalogue.models import Catalogue, CatalogueCategory, Product


admin.site.register(Catalogue)
admin.site.register(CatalogueCategory)
admin.site.register(Product)
