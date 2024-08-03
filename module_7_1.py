# with open('products.txt', 'r', encoding='utf-8') as file:
#     # list_ = file.read()
#     print(file.read())
# exit()
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def add(self, *products):
        checker = []
        list_ = self.get_products()
        if list_:
            checker = list_

        with open(self.__file_name, 'a', encoding='utf-8') as file:

            for product in products:
                if product.name in checker:
                    print(f'Продукт {product.name} уже есть в магазине')
                else:
                    file.write(str(product) + '\n')
                    checker.append(product.name)
            del checker, list_

    def get_products(self):
        with open(self.__file_name, 'r', encoding='utf-8') as file:
            list_ = file.read()
            if list_:
                return list_
            else:
                return None


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
# p4 = Product('Candies', 20.5, 'Cakes')

print(p2)  # __str__

s1.add(p1, p2, p3)

# print('Итого в магазине представлены сл. продукты:')
print('------ продукты --------')
print(s1.get_products())
