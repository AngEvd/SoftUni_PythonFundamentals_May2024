class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product):
        if len(self.storage) < self.capacity:
            Storage.storage.append(product)

    def get_products(self):
        return self.storage
