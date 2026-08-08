class Scoop:
     def __init__(self,flavor,number=1):
          self.flavor=flavor
          self.__price=None
          self.count=0
          self.number_of_scoop=number
     def __str__(self):
        return f"Flavor - {self.flavor}, No of Scoops - {self.number_of_scoop}, Price - {self.__price}"
     
     def set_price(self,price):
          self.__price=price

     def get_price(self):
          return self.__price

     def get_no_of_scoop(self):
          return self.number_of_scoop 
     
     def sold(self):
          self.count+=self.get_no_of_scoop()
          print(f"{self.flavor} scoop sold: {self.count}")

     

class Bowl:
     bowl_number = 0
 
     def __init__(self,max_scoops=3):
          self.__scoop_list=[]
          self.count=0
          self.max_scoops=max_scoops
          Bowl.bowl_number += 1
          self.bowl_id = Bowl.bowl_number

     def get_scoop_list(self):
          return self.__scoop_list

     def set_scoop_list(self,Scoop):
          self.__scoop_list.append(Scoop)
     def remove_scoop(self,scoop):
          self.__scoop_list.remove(scoop)        
     def add_scoops(self, *scoops):
          for Scoop in scoops:
               if self.max_scoops>=sum(scoop.get_no_of_scoop() for scoop in self.__scoop_list)+Scoop.get_no_of_scoop():
                    self.set_scoop_list(Scoop)
                    print(f"{Scoop.flavor} added")

               elif self.max_scoops>sum(scoop.get_no_of_scoop() for scoop in self.__scoop_list):
                    print('no much space')
                    break

               else:
                    print('bowl is full')
                    break

     def display(self):
        total = 0
        for Scoop in self.__scoop_list:
             total += Scoop.get_price()*Scoop.get_no_of_scoop()

        print(f"Total price of bowl: {total}")

     def sold(self):
        for Scoop in self.__scoop_list:
             Scoop.sold()
        
        self.count+=1
        print(f"Bowl {self.bowl_id} sold: {self.count}")
       

choco = Scoop('chocolate',1)
choco.set_price(100)
print(choco)

berry = Scoop('berry',2)
berry.set_price(120)
print(berry)

vanilla = Scoop('vanilla')
vanilla.set_price(150)
print(vanilla)

bowl1 = Bowl()
bowl1.add_scoops(choco)
bowl1.display()
bowl1.add_scoops(berry, vanilla)
bowl1.display()

bowl2=Bowl()
bowl2.add_scoops(berry, vanilla)
bowl2.display()

bowl3=Bowl()
bowl3.add_scoops(berry, choco)
bowl3.display()

bowl4 = Bowl(2)
bowl4.add_scoops(berry)
bowl4.add_scoops(choco)
bowl4.display()

bowl2.display()
bowl1.sold()
bowl2.sold()
bowl4.sold()
bowl1.sold()