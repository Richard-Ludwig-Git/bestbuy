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
        print("--------------------------------------------")
        print(f"Total of {total_quantity} items in store")
        print("--------------------------------------------")


    def get_all_products(self):
        active_products = []
        print("-------------------------------------------------------")
        counter = 1
        for item in self.in_store:
            if item.is_active():
                active_products.append(item)
                print(f"{counter}. ", end="")
                item.show()
                counter += 1

        print("-------------------------------------------------------")

    def order(self, shopping_list):
        total_price = 0
        for item in shopping_list:
            total_price += item[0].buy(item[1])
        return total_price