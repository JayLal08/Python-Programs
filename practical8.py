#WAP to sort a list of names in ascending order.
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
t = sorted(arr)
print("Sorted array = ",t)