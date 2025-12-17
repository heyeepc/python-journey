def shipping_cost(quantity):
    if quantity <= 0:
        return 0
    return 10.95 + (quantity - 1) * 2.95
