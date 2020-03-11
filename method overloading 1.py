"""
method overloading
"""

class sample:
    def addition(self,*n): #*n= providing of n number of parameters
        sum=0
        for i in n:
            sum=sum+i
        print("Sum:",sum)
s1=sample()
s1.addition()                       #Method name is same but no of paramters aare different
s1.addition(10,20)
s1.addition(10,20,30,40)
s1.addition(10,20,30,40,50,60)




"""
deposit  method overloading is remaining 
 cheque deposit 
 dd deposit
 gold deposit
 cash deposit
"""
