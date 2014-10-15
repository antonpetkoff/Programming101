
class Product(object):

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price

class Laptop(Product):

    def __init__(self, name, stock_price, final_price, diskspace, RAM):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.RAM = RAM

class Smartphone(Product):

    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels

class Store(object):

    def __init__(self, name):
        self.name = name
        self.products = {}

    def load_new_products(self, product, count):
        if isinstance(product, Product):
            key = product
            if key in self.products.keys():
                self.products[key] += count
            else:
                self.products[key] = count

    def list_products(self, product_type):
        for key in self.products.keys():
            if isinstance(key, product_type):
                print(key.name + " - " + str(self.products[key]))

    def

def main():
    new_product = Product('HP HackBook', 1000, 1243)
    print(new_product.profit())

    store = Store('Laptop.bg')
    smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
    laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
    store.load_new_products(smarthphone, 20)
    store.load_new_products(laptop, 10)

    store.list_products(Laptop)

if __name__ == '__main__':
    main()
