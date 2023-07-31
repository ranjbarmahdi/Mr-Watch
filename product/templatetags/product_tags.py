from django import template
from..models import Product, Comment
from random import sample

register = template.Library()


# =======================================<< Related Products >>=======================================
@register.simple_tag()
def related_products(brand: str, dial_type: str, engine_type: str, count=6):

    if brand:
        products = Product.published.filter(brand=brand)

    if dial_type:
        products |= Product.published.filter(dial_type=dial_type)

    if engine_type:
        products |= Product.published.filter(engine_type=engine_type)

    return sample(products, count)


# =======================================<< Seller Other Products >>=======================================
@register.simple_tag()
def seller_other_products(id, count=5):
    return Product.published.filter(seller__id=id)

