#WAP to read all set of nos. from keyboard & to find the sum
#of all the elements of the given array using a function.

arr =[]
n=int(input("Enter the number the element:")) 
for i in range(n):
    arr.append(int(input("Enter the elements:")))

def sum():

   s = 0
   for i in arr :
    s=s+i
   print("sum = ",s)
print("The list is : ",arr)
sum()