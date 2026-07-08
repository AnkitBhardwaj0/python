from ast import Break
import random
class FlashCard:
    def __init__(self):
        self.fruits = {
            "Apple": "Red","Banana": "Yellow","Orange": "Orange","Grapes": "Green","Mango": "Yellow","Strawberry": "Red","Watermelon": "Green","Pineapple": "Brown","Papaya": "Orange","Kiwi": "Brown","Cherry": "Red","Blueberry": "Blue","Blackberry": "Black","Guava": "Green","Lemon": "Yellow","Lime": "Green","Peach": "Pink","Pear": "Green","Pomegranate": "Red","Coconut": "Brown"
                       } 
        
    def display(self):
        print("welcome to fruit quiz")
        while True:
            fruit=random.choice(list(self.fruits.keys()))
            print(f"What is the colour of {fruit}?")
            colour=input("enter fruit colour")
            if self.fruits[fruit].lower() == colour.lower():
                print("correct answer")
            else:
                print("incorrect answer")
            try:
                num=int(input("Enter 0, if you want to play again"))
                if num!=0:
                    break
            except ValueError:
                break 

new_user=FlashCard()
new_user.display()

        