from database import db_get_all_products, db_add_product, db_get_product, db_update_product, db_delete_product

class Product:
    def __init__(self, id, name, price, quantity):
      self.id = id
      self.name = name
      self.price = price
      self.quantity = quantity

    def update(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
          'id': self.id,
          'name': self.name,
          'price': self.price,
          'quantity': self.quantity
        }


class Inventory:
    def __init__(self):
      pass
    def add_product(self, name, price, quantity):
      db_add_product(name, price, quantity)

    def get_product(self, product_id):
      product = db_get_product(product_id)
      if product:
        return Product(product['id'],product['name'], product['price'], product['quantity'])
      return None
    def update_product(self, product_id, name, price, quantity):
      db_update_product(product_id, name, price, quantity)
      return self.get_product(product_id)

    def delete_product(self, product_id):
      return db_delete_product(product_id)

    def get_all_products(self):
      products = db_get_all_products()
      return {p['id']: Product(p['id'],p['name'], p['price'], p['quantity']) for p in products}