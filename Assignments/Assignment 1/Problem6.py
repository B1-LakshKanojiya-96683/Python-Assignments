#6] Write a Python Program Get age input from user and check if user is eligible for voting

age = int (input("Enter your age to check voting eligbility"))
if age >=18:
    print(f"You are eligible for voting in the Elections !")
elif age >=0 and age<18:
    print("You are not eligible for voting")
else:
    print("The age that you have entered is invalid")

