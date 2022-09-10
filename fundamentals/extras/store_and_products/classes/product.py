class Product:
    unique_id = 0
    product_list = []

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.unique_id = Product.unique_id
        Product.unique_id += 1

    def __repr__(self):
        return f'{self.name} is a type of {self.category} that costs {self.price} each. The unique ID is {self.unique_id}...'

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price *= (1 + percent_change)
        else:
            self.price *= (1 - percent_change)

        return self

    def print_info(self):
        print(self.name)
        print(self.category)
        print(self.price)
        return self

