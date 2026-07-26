"""
 You are given a function definition. There might be several issues on execution of this function. You are asked to do exception handling for diffrent errors that this function goes in to `without altering this function`. And print error text.
"""
def function(l: list, s, **args):
    last_element = l[-1]
    
    l[int(s)]=10
    any_element = l[int(s)+10]
    l[s]=10
    
    res = sum(l)
    
    p = args['p']
    # print(p)
    return res/last_element * p + any_element
def check(func,*args,**kwargs):
    try:
        print(func(*args,**kwargs),"\n")
        print(" this is result\n")

    except Exception as e:
        print("Exception:- \n")
        print(e,"\n")


check(function,[1,2,1], 12)
check(function,[1,2,1]*9,'1-2')
check(function,[1,'2',1]*9, 12)
check(function,[1,'2',1]*9, 12)
check(function,[1,2,0]*9, 12  )
check(function,[1,2,1]*9, 12, p=None)
check(function,[1,2,0]*9, 12, p=10)