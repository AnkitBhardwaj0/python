#Ice-Cream Scoops and Bowl shop
"""
###`Q-6:` Ice-Cream Scoops and Bowl shop

1. Create a class `Scoop` which has one public property `flavor` and one private proptery `price`. Take `flavor` values during object creation.
2. Create a class `Bowl` with private prperty `scoop_list` which will have list of scoopd object. 
3. Create a method `add_scoops` in `Bowl` class which will add any no of `Scoop` objects given as parameter and store it in `scoops_list`.
4. Make getter and setter method for `price` property.
5. Make a method `display` to display `flavour` and `price` of each `Scoop` in `scoop_list` and print total price of the bowl by adding all flavour scoops prices.

6. Make a method `sold` in both `Scoop` class and `Bowl` class to print no of quantity sold.
"""
class Scoop:
     def __init__(self,flavor):
          self.flavor=flavor
          self.__price=None
          self.count=0

     def set_price(self,price):
          self.__price=price

     def get_price(self):
          return self.__price
     
     def sold(self):
          self.count+=1
          print(f"{self.flavor} scoop sold: {self.count}")

class Bowl:
     def __init__(self):
          self.__scoop_list=[]
          self.count=0

     def get_scoop_list(self):
          return self.__scoop_list

     def set_scoop_list(self,scoops):
          self.__scoop_list.extend(scoops)
              
     def add_scoops(self, *scoops):
        self.set_scoop_list(scoops)

     def display(self):
        total = 0

        for Scoop in self.__scoop_list:
            print(f"Flavor: {Scoop.flavor}")
            print(f"Price: {Scoop.get_price()}")

            total += Scoop.get_price()

        print(f"Total price of bowl: {total}")

     def sold(self):
        self.count += 1
        print(f"Bowl sold: {self.count}")

s1 = Scoop("Vanilla")
s2 = Scoop("Chocolate")
s3 = Scoop("Strawberry")

s1.set_price(50)
s2.set_price(60)
s3.set_price(40)

b1 = Bowl()
b1.add_scoops(s1, s2, s3)
b1.display()

s1.sold()
s1.sold()

b1.sold()
b1.sold()