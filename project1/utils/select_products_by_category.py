def select_products_by_category(products, category):
    select_products = []
    for product in products:
        if product.category == category:
            select_products.append(product)
    
    return select_products
