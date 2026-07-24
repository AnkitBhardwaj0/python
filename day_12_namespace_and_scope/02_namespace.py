"""
 Write a program to show namespace of object/instance of above(Person) class.
"""
class person:
    def __init__(self,name,state,city,age):
        self.name=name
        self.state=state
        self.__city=city
        self.__age=age
        
    def address(self):
        print(f"name of person is {self.name}")
        print(f"state : {self.state}")
        print(f"city : {self.__city} ")
p1=person("amit","bihar","patna",22)
p1.address()
print(p1.__dict__)
print("\n\n")
print(person.__dict__)