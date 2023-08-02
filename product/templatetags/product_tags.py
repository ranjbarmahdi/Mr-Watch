from django import template
from ..models import Product, Comment
from random import sample
from django.db.models import Q

register = template.Library()


# =======================================<< Related Products >>=======================================
@register.simple_tag()
def related_products(product, count=6):
    products = Product.published.filter(
        Q(brand=product.brand) | Q(dial_type=product.dial_type) | Q(engine_type=product.engine_type))
    products = list(products.distinct())

    return sample(products, l if (l := len(products)) < count else count)


# =======================================<< جدیدترین محصولات >>=======================================
@register.simple_tag()
def latest_products(count=6):
    return Product.published.all().order_by('-publish')[:count]
