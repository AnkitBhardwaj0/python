"""
Write a program that uses datetime module within a class. Enter manufacturing date and expiry date of the product. The program must display the years, months and days that are left for expiry.
"""
from datetime import date
class Product:

     def __init__(self,manufacture,expiry):
          self.manufacture_date=manufacture
          self.expiry_date=expiry
     def days_left(self):
          difference=self.expiry_date-self.manufacture_date
          self.years=difference.days//365
          self.months=(difference.days%365)//30
          self.days=(difference.days%365)%30
          return 
     def show(self):
          self.days_left()
          print("left time")
          print(f"years : {self.years}")
          print(f"months : {self.months}")
          print(f"days : {self.days}")
manufacture = date.fromisoformat(
    input("Enter manufacturing date (YYYY-MM-DD): "))
expiry=date.fromisoformat(input("enter expiry date (YYYY-MM-DD): "))
sprite=Product(manufacture,expiry)
sprite.show()

     

     

