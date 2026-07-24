"""
Iterate in circle
Define a class, `Circle`, that takes two arguments when defined: a sequence and a number. The idea is that the object will then return elements the defined number of times.
"""
class circle:
    def __init__(self,sequence,number):
        self.sequence=sequence
        self.loop=number

    def __iter__(self):
        return iterator_circle(self)

class iterator_circle:
    def __init__(self,iterator_obj):
        self.iterator=iterator_obj
        self.index=0
        self.out=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterator.loop<=self.index:
            raise StopIteration
        current=self.iterator.sequence[self.out]
        self.out+=1
        self.index+=1
        self.out=self.out%len(self.iterator.sequence)

        return current
    
        
c = circle('abc', 5)  
print(list(c))    
b = circle('abc', 10)  
print(list(b))   
