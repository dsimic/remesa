from catalogue.models import (Catalogue, CatalogueCategory, Product,
                              FeaturedProduct)

# create catalogue

Catalogue.objects.all().delete()

catalogue = Catalogue(
    name="LaRemesa Main",
    slug="laremesa-main",
    publisher="La Remesa",
    description="Main catalogue")

catalogue.save()

# create two categories

fine_produce = CatalogueCategory(
    catalogue=catalogue,
    name="Fresh Produce",
    slug="fresh-produce",
    description="Fresh local produce.")

fine_produce.save()


artisinal_foods = CatalogueCategory(
    catalogue=catalogue,
    name="Artisinal Foods",
    slug="artisinal-foods",
    description="Artisinal foods.")

artisinal_foods.save()


# create two products
from django.core.files import File


granola = Product(
    category=artisinal_foods,
    name="Gourmet Granola",
    slug="gourmet-granola",
    description="Liliana's gourmet granola.",
    price_in_cop=18.000)

granola.photo.save("granola.gif", File(open("img/granola_foto.gif")))

granola.save()


eggs = Product(
    category=fine_produce,
    name="Big Red Eggs",
    slug="big-reg-eggs",
    description="Super red yolks from uber healthy chickens.",
    price_in_cop=6.000)

eggs.photo.save("huevos_foto.jpg", File(open("img/huevos_foto.jpg")))

eggs.save()


# create featured products

fgranola = FeaturedProduct(product=granola)
fgranola.save()

feggs = FeaturedProduct(product=eggs)
feggs.save()
