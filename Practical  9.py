def arrsum(a):
    s = 0
    for i in a:
        s=s+i 
    return s 
a = []
n = int(input("Enter the no. of elements :"))
for i in range(n):
    a.append(int(input("Enter value : ")))
sum = arrsum(a)
print("sum = ",sum)