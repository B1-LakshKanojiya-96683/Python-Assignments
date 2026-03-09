class Student:
    def __init__(self, roll_no, name , math, physics, chemistry):
        self.roll_no=roll_no
        self.name=name
        self.math=math
        self.physics=physics
        self.chemistry=chemistry

    def set_name(self, name):
        self.name = name
    def set_math(self, m):
        self.math = m
    def set_physics(self, p):
        self.physics = p 
    def set_chemistry(self, c):
        self.chemistry = c

    def get_roll_no(self):
        return self.roll_no
    def get_name(self):
        return self.name
    def get_math(self):
        return self.math
    def get_chemistry(self):
        return self.chemistry
    def get_physics(self):
        return self.physic
    def calculate_total(self):
        return self.physics + self.chemistry + self.math
        
    def calculate_percentage(self):
        self.percentage = (self.physics + self.chemistry + self.math) / 300 * 100
        return self.percentage
        
    def has_passed(self):
        return self.calculate_percentage() >= 40

class execute:
    E = Student("CBR5", "Saitama", 44, 21, 9)
    print(f"Your percentage is {E.calculate_percentage()}")
    print(f"Your passing status is {E.has_passed()}")