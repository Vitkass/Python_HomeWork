def select_products_by_category(products:list, category:str)->list:
    select_products = []
    for product in products:
        if product.category == category:
            select_products.append(product)
    
    return select_products
