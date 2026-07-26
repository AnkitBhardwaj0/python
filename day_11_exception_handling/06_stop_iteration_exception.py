"""
Write a python function which infinitely prints natural numbers in a single line. Raise the **StopIteration** exception after displaying first 20 numnbers to exit from the program.
"""
def infinitely():
    number=1
    while(True):
        try:
            print(number)
            number+=1
            if number>20:
                raise StopIteration("\n20 numbers printed finished")
        except StopIteration as e:
            print(e)
            break
        
infinitely()