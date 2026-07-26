"""
Cast vote
Write a program that validate name and age as entered by the user to determine whether the person can cast vote or not. To handle the age, create **InvalidAge** exception and for name, create **InvalidName** exception. The name will be invalid when the string will be empty or name has only one word.
"""
class InvalidAge(Exception):
    def __init__(self,age):
        self.age=age
        super().__init__(f"{age} under age person cannot vote")
class InvalidName(Exception):
    def __init__(self,name):
        self.name=name
        super().__init__(f"invalid {name} can not vote")

try:
    name=input("Enter the name : ")
    age=int(input("Enter the age : "))
    if len(name.split())<2 :
        raise InvalidName(name)
    elif age<18:
        raise InvalidAge(age)
    else:
        print(f"{name}  Congratulation !!! You can vote.")
except InvalidAge as e:
    print(e)
except InvalidName as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)