"""
You are given a code snippet. There might be several issues on execution of this code. You are asked to do exception handling for diffrent errors, condition is what ever happens we need to execute last line printing correct result of `sum of elements`.
l = [{0:2},2,3,4,'5', {5:10}]
# For calculating sum of above list
s=0
for i in range(len(l)):
    #You can Edit code from here
    s += l[i].get(i)
    s += l[i]
    s += int(l[i])
print(s)
"""
from sqlite3 import DataError


l = [{0:2},2,3,4,'5', {5:10}]
# For calculating sum of above list
s=0
for i in range(len(l)):
    #You can Edit code from here
    try:
        if type(l[i])==dict:
            s += l[i].get(i)
        if type(l[i])==str:
            s += int(l[i])

        s += l[i]
           
    except AttributeError as e:
        print(f"exception found :- {e} \n")
    except TypeError as e:
        print(f"exception found :- {e} \n")   
print(s)