"""
Write a recursive program to to calculate `gcd` and print no. of function calls taken to find the solution.
gcd(5,10) -> result in 5 as gcd and function call 3
"""
def gcd(num1,num2,count):
    
    if num2!=0:
        num1,num2=num2,num1%num2
        return gcd(num1,num2,count+1)
    if num2==0:
        return num1,count

def show(num1, num2):
    gcd_value, function_calls = gcd(num1, num2, 1)
    print(f"GCD: {gcd_value}")
    print(f"Function Calls: {function_calls}")

show(5,25)