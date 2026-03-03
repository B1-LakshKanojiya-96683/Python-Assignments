#8) Write a program that will calculate the price for a quantity entered from the keyboard, given that the 
# unit price is Rs 5 and there is a discount of 10 percent for quantities over 30 and a 15
#percent discount for quantities over 50.

quantity = int (input ("Enter the quantity"))

def calculate_price(qt):
    if qt<=30:
        price = qt*5
        return price
    
    elif qt >30 and qt <=50:
        price = 30*5 + 4.5*(qt-30)
        return price
    
    elif qt > 50:
        price = 30*5 + 4.5*20 + (5-0.75)*(qt-50)
        return price
    else:
        print("wrong input")

result=calculate_price(quantity)
print(f"the final price is {result}")