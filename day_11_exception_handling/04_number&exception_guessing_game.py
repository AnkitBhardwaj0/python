"""
Number game program.
Write a number game program. Ask the user to enter a number. If the number is greater than number to be guessed, raise a **ValueTooLarge** exception. If the value is smaller the number to be guessed the, raise a **ValueTooSmall** exception and prompt the user to enter again. Quit the program only when the user enters the correct number. Also raise **GuessError** if user guess a number less than 1.
"""
import random
class GuessError(Exception):
    pass
class ValueTooLargerError(Exception):
    pass
class ValueTooSmallerError(Exception):
    pass
random_number=random.randint(1,100)
while True:
    
    try:
        guess_number=int(input("guess the number : "))
        if random_number==guess_number:
            print("you guessed the number : ")
            break
        elif guess_number<1:
            raise GuessError("guess number cannot be less than 1 ")
        elif random_number<guess_number:
            raise ValueTooLargerError("guess number is greater ")
        elif random_number>guess_number:
            raise ValueTooSmallerError("guess number is smaller ")
        else:
            raise ValueError
    except GuessError as e:
        print(e)
        print("try again ! \n")
    except ValueTooLargerError as e:
        print(e)
        print("try again ! \n")
    except ValueTooSmallerError as e:
        print(e)
        print("try again ! \n")
    except ValueError as e:
        print(e)
        print("try again ! \n")



