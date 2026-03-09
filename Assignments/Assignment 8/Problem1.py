'''
Create a class named Mobile with attributes ModelName,Company,Price and with
methods:set_attributes, print_details and can_afford  '''

class Mobile:
    def __init__(self):
        pass
    def set_attributes(self,Name, Comp, p):
        self.ModelName = Name
        self.Company= Comp
        self.Price=p

    def print_details(self):
        print(f"The name of the car is   {self.ModelName}")
        print(f"The name of the company is {self.Company}")
        print(f"The price of the car {self.ModelName}  is   {self.Price}")

    def can_afford(self):
        budget=int(input("Enter your budget"))
        if self.Price>budget:
            print("This car is unfortunately not Affordable")
        else:
            print("This car is absolutely Affordable")

class Execute:
    m=Mobile()
    m.set_attributes("812 SuperFast Competetizione", "Ferrari", 1600000)                #  price is in USD
    m.print_details()
    m.can_afford()