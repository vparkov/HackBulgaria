class Product:
    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        if(self.final_price - self.stock_price > 0):
            print(self.final_price - self.stock_price)
        else:
            print(False)

    def __str__(self):
        return "{} {} {}".format(self.name, self.stock_price, self.final_price)


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, ram):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.ram = ram

    def print_laptop(self):
        print(self.name, self.stock_price, self.final_price, self.diskspace, self.ram)

    #def __str__(self):
    #    return "Name: {}, HDD: {}".format(self.name, self.diskspace)


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels

    def print_smartphone(self):
        print(self.name, self.stock_price, self.final_price, self.display_size, self.mega_pixels)

    #def __str__(self):
    #   return "Name: {}, HDD: {}, Display Size: {}, Mega Pixels: {}".format(self.name, self.display_size, self.mega_pixels)


class Store():
    def __init__(self, name):
        self.name = name
        self.items = {}

    def load_new_products(self, item, count):
        if item in self.items:
            self.items[item] += count
        else:
            self.items[item] = count

    def list_products(self, item_class):
        for item in self.items:
            if isinstance(item, item_class):
                print(item)

    def sell_product(self, product):
        for item in self.items:
            if self.items[product] > 0:
                return True
            else:
                return False


def main():
    print("\n")
    new_product = Product('HP HackBook', 1000, 1243)
    new_product.profit()

    new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
    new_laptop.print_laptop()

    new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
    new_smarthphone.print_smartphone()

    print("\npishka\n\n=======YOU ARE IN THE STORE NOW!==========\n")

    new_store = Store('Laptop.bg')
    new_store.load_new_products(new_smarthphone, 20)
    new_store.load_new_products(new_laptop, 20)
    new_store.list_products(Smartphone)
    new_store.list_products(Laptop)

    #print("8 sell product\n")

    #store = Store('Laptop.bg')
    #smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
    #store.load_new_products(smarthphone, 2)
    #print(store.sell_product(smarthphone)) # True
    #print(store.sell_product(smarthphone)) # True
    #print(store.sell_product(smarthphone)) # False

if __name__ == '__main__':
    main()