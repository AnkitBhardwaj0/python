"""
Class Name - Person
Attributes:
name - public
state - public
city - private
age - private
Methods:
address - public
It give address of the person as "<name>, <city>, <state>"
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