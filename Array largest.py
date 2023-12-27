#WAP to read a set of numbers in an array & to find the largest of them

a = int(input("Enter the length or array"))
arr =[]
for i in range(a):
    a = int(input())
    arr.append(a)
print("arr =",arr)

for i in arr:
    if i is max:
        max=i 
print(max(arr))