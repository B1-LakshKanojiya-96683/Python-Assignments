"""
4.Create a class product having (pid and manufacture_location) as private fields,

Create another class as Book having (name, number_of_pages,author,price) as private fields. 

Specify _init(), getters, setters, __str_() , print_data() Use correct OOP feature to implement this scenario.
a) display the details of the product and book
b) check if book price is 0 or negative then price is not valid otherwise print valid price.
"""

class Product:
    
    def __init__(self, pid, manufacture_location):
        self.__pid = pid
        self.__manufacture_location = manufacture_location

    def get_pid(self):
        return self.__pid
    def set_pid(self, pid):
        self.__pid = pid
    def get_manufacture_location(self):
        return self.__manufacture_location
    def set_manufacture_location(self, manufacture_location):
        self.__manufacture_location = manufacture_location
    def __str__(self):
        return f"PID: {self.__pid}, Manufacture Location: {self.__manufacture_location}"

class Book(Product):
    def __init__(self, pid, manufacture_location, name, number_of_pages, author, price):
        super().__init__(pid, manufacture_location)
        self.__name = name
        self.__number_of_pages = number_of_pages
        self.__author = author
        self.__price = price

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    def get_number_of_pages(self):
        return self.__number_of_pages
    def set_number_of_pages(self, number_of_pages):
        self.__number_of_pages = number_of_pages
    def get_author(self):
        return self.__author
    def set_author(self, author):
        self.__author = author
    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"{super().__str__()}, Book Name: {self.__name}, Pages: {self.__number_of_pages}, Author: {self.__author}, Price: {self.__price}"

    def print_data(self):
        print(self.__str__())
        if self.__price <= 0:
            print("Price is not valid")
        else:
            print("Valid price")


# these statements are written to demonstrate execution
b1 = Book(101, "London", "Python Mastery", 450, "Jane Doe", 29.99)
b1.print_data()