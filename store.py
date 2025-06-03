import product

class Store:
    in_store = []

    def __init__(self, item_list):
        self.in_store = item_list

    def remove_product(self, product):
        if product in Store.in_store:
            Store.in_store.remove(product)


    def get_total_quantity(self):
        total_quantity = 0
        for item in self.in_store:
            total_quantity += item.Quantity
        return total_quantity


    def get_all_products(self):
        active_products = []
        for item in self.in_store:
            if item.is_active():
                active_products.append(item)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for item in shopping_list:
            total_price += item[0].buy(item[1])
        return total_price