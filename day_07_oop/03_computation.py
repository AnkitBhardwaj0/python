class computation:
    def __init__(self):
        pass
    
    def factorial(self,number):
        fact=1
        for i in range(1,number+1):
            fact*=i

        return fact
    
    def naturalSum(self,number):
        total=0
        for i in range(1,number+1):
            total+=i

        return total

    def testPrime(self,num):
        if num<=1: 
            return False
        for i in range(2,int(num**0.5+1)):
            if num%i==0:
                return False 
            
        return True

    def testCo_Prime(self,num1,num2):
        a, b = num2, num1
        while b!=0:
            a,b=b,a%b

        if a==1:
            return f"{num1} and {num2} are co-prime of each other"
        else:
            return f"{num1} and {num2} are not co-prime of each other"
          
    def tableMult(self,num):
        for i in range(1,11):
            print(f"{num} X {i} = {i*num}")
    
    def allTableMult(self):
        for i in range(1,10):
            self.tableMult(i)
            print()
    
    def listdiv(self,num):
        div=[]
        for i in range(1,int(num**0.5+1)):
            if num%i==0:
                div.append(i)
                if num//i!=i:
                    div.append(num//i)
        return sorted(div)
    
    def listdivprime(self,num):
        primediv=[]
        for i in self.listdiv(num):
            if self.testPrime(i):
                primediv.append(i)
        return primediv
    
cal=computation()
print(cal.listdiv(5))
print()
cal.tableMult(5) 
print()
print(cal.listdivprime(5))         

                
