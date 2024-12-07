'''
Create a Triangle class that accepts three side-lengths of the triangle as a, b and c as
parameters at the time of object creation. Class Triangle should have the following:

1. Is_valid(): Returns valid if the given sides can form a triangle, otherwise returns invalid.
2. Side_Classification(): Return invalid if triangle is invalid. Returns the type of triangle based on the sides (equilateral, isosceles, or scalene).
3. Angle_Classification(): Return invalid if triangle is invalid. Returns the type of triangle based on the angles (acute, obtuse, or right-angled).
4. Area(): Return invalid if triangle is invalid. Returns the area of the triangle.
'''

# Solution
import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def Is_valid(self):
        if self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b:
            return 'Valid'
        else:
            return 'Invalid'
    
    def Side_Classification(self):
        if self.Is_valid() == 'Invalid':
            return 'Invalid'
        elif self.a == self.b == self.c:
            return 'Equilateral'
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return 'Isosceles'
        else:
            return 'Scalene'
    
    def Angle_Classification(self):
        if self.Is_valid() == 'Invalid':
            return 'Invalid'
        a, b, c = sorted([self.a, self.b, self.c])
        if a**2 + b**2 > c**2:
            return 'Acute'
        elif a**2 + b**2 == c**2:
            return 'Right-angled'
        else:
            return 'Obtuse'
    
    def Area(self):
        if self.Is_valid() == 'Invalid':
            return 'Invalid'
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Sample Testcase
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())
