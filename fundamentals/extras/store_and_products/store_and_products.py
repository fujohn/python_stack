from classes.store import Store
from classes.product import Product

milk = Product('milk', 10, 'dairy')
cheese = Product('cheese', 20, 'dairy')
detergent = Product('detergent', 30, 'cleaning')
shampoo = Product('shampoo', 15, 'bath')

target = Store('target', [milk, cheese, detergent, shampoo])