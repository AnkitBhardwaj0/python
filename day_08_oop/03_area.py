#Find the area of a rectangle.
class Rectangle:

     def __init__(self,length,height):
          self.length=length
          self.height=height

     def area(self):
          return self.length*self.height

     def is_Square(self):
          return True if self.length==self.height else False

length=int(input("enter length : "))
height=int(input("enter height : "))

a=Rectangle(length,height)
print(a.is_Square())
print(a.area())