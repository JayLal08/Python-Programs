#WAP to implement selection in python where input is taken from user

n=int(input("enter the length :"))
arr=[]
for i in range(n):
    a=int(input("Enter element:"))
    arr.append(a)
print(f"List is: {arr} ")


for j in range(len(arr)):
 min=j

 for i in range(j+1,len(a)): 
    if(arr(min)>arr(i)):    
        min=i

 temp = arr[j]
 arr[j] = arr[min]
 arr[min] = temp
print(arr)