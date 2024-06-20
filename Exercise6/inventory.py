class Inventory:
    def __init__(self, capacity: int):
        self.items = []
        self.__capacity = capacity

    def add_item(self, item: str):
        if len(self.items) < self.__capacity:
            self.items.append(item)
        else:
            return f"not enough room in the inventory"

    def get_capacity(self):
        return self.__capacity

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {len(self.items) - self.__capacity}"
