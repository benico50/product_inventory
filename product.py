""" A class to manage inventory products """


class Product:
    """ Creates a single product """
    def __init__(self, name, price, prod_id, quantity):
        self.name = name
        self.price = price
        self.prod_id = prod_id
        self.quantity = quantity
