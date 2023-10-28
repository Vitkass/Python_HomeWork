def extract_prices(products:list)->list:
    prices = []
    for product in products:
        prices.append(product.price)
    
    return prices
