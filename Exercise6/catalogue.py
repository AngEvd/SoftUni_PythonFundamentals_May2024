class Catalogue:
    products = []

    def __init__(self, name: str):
        self.name = name

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str) -> list:
        return list(filter(lambda x: x.startswith(first_letter), self.products))

    def __repr__(self):
        self.products.sort()
        return (f"Items in the {self.name} catalogue:\n" +
                f"\n".join(self.products))


