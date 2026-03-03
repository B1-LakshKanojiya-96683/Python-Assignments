#Q1: Write a function check_voter(name: str, age: int) that:

   #Uses a lambda to check if age ≥ 18

   #Returns True if eligible, otherwise False

   #Prints the eligibility message

  # Call the function for three people.

Name = input ("Enter your name")
Age = int (input("Enter your age"))

def check_voter(name, age):
    agechecker=lambda age_check : age_check>=18
    print(f"{agechecker(age)}")

check_voter(Name, Age)