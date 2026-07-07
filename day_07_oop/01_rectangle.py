class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.breadth=width
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def area(self):
        return self.length*self.breadth
    def display(self):
        print("The length of rectangle is: ",self.length)
        print("The width of rectangle is: ",self.breadth)
        print("The perimeter of rectangle is: ",self.perimeter())
        print("The area of rectangle is: ",self.area())
rect=rectangle(3,4)
rect.display()