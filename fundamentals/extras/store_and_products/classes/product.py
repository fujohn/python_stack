class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __repr__(self):
        return f'{self.name} is a type of {self.category} that costs {self.price} each.'