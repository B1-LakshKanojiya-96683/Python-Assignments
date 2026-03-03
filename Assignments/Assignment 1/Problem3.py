#Write a program to accept a 4 digit number and
#   a. Display face value of each decimal digit
#   b. Display place value of each decimal digit
#   c. Display no in reverse order by changing decimal place values.

#floor division

num = int(input("Enter the 4 digit number      "))
backup_num=num
if num >=1000  and num <=9999:
    
    print("Now displaying the face value of each digit")
    for x in range (3,-1,-1):
          face_value=int(num/(10**x))
          num = num - face_value*(10**x)
          print(f"{face_value}")
    
    print("        ")
    print("Now printing the place value of each digit ")
    num = backup_num
    for x in range (3,-1,-1):
          fv=int(num/(10**x))
          num = num - fv*(10**x)
          place_value= fv*(10**x)
          print(f"{place_value}")
    
    print("     ")
    print("Now reversing the number and printing it")
    
    reverse =0
    num = backup_num
    for x in range (3,-1,-1):
        last_digit= num%10
        num=int(num/10)
        reverse=reverse+last_digit*(10**x)
    print(f"The reversed number is   {reverse}")


else:
        print("This is not a four digit number please try again")
