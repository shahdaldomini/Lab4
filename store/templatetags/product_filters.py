from django import template

register = template.Library()


@register.filter
def upper_text(value):
    return value.upper()


@register.filter
def title_text(value):
    return value.title()


@register.filter
def short_description(value):
    if len(value) > 50:
        return value[:50] + "..."
    return value


@register.filter
def price_format(value):
    return str(value) + " ريال"


@register.filter
def product_status(value):
    if value:
        return "متوفر"
    return "غير متوفر"


@register.filter
def product_search(products, keyword):

    if not keyword:
        return products

    keyword = keyword.lower()

    result = []

    for product in products:

        if (
            keyword in product.name.lower()
            or keyword in product.brand.lower()
            or keyword in product.description.lower()
        ):
            result.append(product)

    return result