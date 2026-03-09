"""2.
Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r using the constructor:
def init (self,a,b,r):
self.a = a
self.b = b
self.r =r                                                                                                                                                                                                                                                     #commit add push
A:- Define a Area() method of the class which calculates the area of the circle.
B:- Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.
"""


class Circle:
    def __init__(self,a,b,r):
        self.a=a
        self.b=b
        self.r=r
        circleC=([self.a,self.b],self.r)

    def area(self):
        Area =3.14*(self.r**2)
        print(f"The area of the circle is {Area}")

    def Perimeter(self):
        perimeter=2*3.14*self.r
        print(f"The perimeterof the circle is this {perimeter}")

class Execute:
    
    x=int(input("Enter the x coordinate of origin"))
    y= int(input("Enter the y coordinate of origin"))
    rad=int(input("Enter the radius of the circle"))

    Circ=Circle(x,y,rad)

    Circ.area()
    Circ.Perimeter()
    