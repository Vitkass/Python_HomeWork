from models.product import Product

def price_sorted(product:Product)->int:
    return product.price


def get_ordered_products_by_price(products:list)->list:
    return sorted(products, key=price_sorted, reverse=True)
