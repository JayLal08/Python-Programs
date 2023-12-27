from re import A


def fact(a):
    
    fact = 1
    a = 1
    while(a>=1):
        
        fact = fact * a 
        a = a + 1
    return fact 
a = int(input("Enter a number"))
t = fact(a)
print(t)