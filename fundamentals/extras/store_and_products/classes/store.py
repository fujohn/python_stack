class Store:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def __repr__(self):
        return f'{self.name} has {self.products}'