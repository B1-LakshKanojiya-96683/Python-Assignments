# Write a program that prompts the user to input number of calls and calculate the monthly telephone bills as per the following rule:
  # Minimum Rs. 200 for up to 100 calls.
   #Plus Rs. 0.60 per call for next 50 calls.
   #Plus Rs. 0.50 per call for next 50 calls.
   #Plus Rs. 0.40 per call for any call beyond 200 calls.


calls= int(input("enter the number of calls you have had"))
if calls <=100:
    bill = 200
    print(f"your bill is    {bill}")

elif calls > 100 and calls <=150:
    bill = 200 + 0.60*(calls - 100)

elif calls >150 and calls <=200:
    bill = 200 + 50*0.60 + 0.50*(calls - 150)


elif calls > 200:
    bill = 200 + 0.60*50 + 0.50*50 + 0.40*(calls - 200)


else :
    print("invalid input from your side")

print(f"Your Bill is {bill}")