#01] Write a Python Program find an area of a rectangle and perimeter of the rectangle.

length = int(input("enter the rectangle length    ") )
breadth = int(input("enter the rectangle breadth    "))

perimeter = 2*(length + breadth)
area = length*breadth
print(f"the perimeter is {perimeter}" + "  and  " + f"the area is {area}")
