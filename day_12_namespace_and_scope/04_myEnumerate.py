"""
Create MyEnumerate class
"""
class myEnumerate:
    def __init__(self,item):
        self.object=item
    def __iter__(self):
        return obj_myEnumerate(self)
    
class obj_myEnumerate:
    def __init__(self,iterator):
        self.iterator=iterator
        self.index=0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.iterator.object):
            raise StopIteration
        current = self.iterator.object[self.index]
        current_index=self.index
        self.index += 1
        return (current_index,current)
        
l=range(1,10)  
c=myEnumerate(l)
for i in c:
    print(i)