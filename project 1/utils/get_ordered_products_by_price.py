def price_sorted(product):
    return product.price


def get_ordered_products_by_price(products):
    return sorted(products, key=price_sorted, reverse=True)
