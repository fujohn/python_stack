class Store:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def __repr__(self):
        return f'{self.name} has {self.products}'

    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, unique_id):
        for i in range(len(self.products)):
            if self.products[i].unique_id == unique_id:
                self.products.pop(i)
                break
        return self

    def inflation(self, percent_increase):
        for product in self.products:
            product.update_price(percent_increase, True)
        return self

    def set_clearance(self, category, percent_discount):
        for product in self.products:
            if product.category == category:
                product.update_price(percent_discount, False)
        return self