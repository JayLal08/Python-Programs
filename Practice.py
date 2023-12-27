#purse = dict()
#purse['money'] = 12
#purse['Calculator'] = 1
#purse['perfume'] = 2
#purse['tissue'] = 10
#print(purse['money'])
#print(purse['Calculator'])
#print(purse['perfume'])
#print(purse['tissue'])

#a = set()
#a.add(1)
#a.update([2,3])
#a.discard(2)
#a.remove(1)
#print(a)

#A = {1,2,3}
#B = {3,4,5}
#print(A|B)
#print(A&B)
#print(A-B)
#print(A^B)

#a = 4
#b = 3
#print(+a)
#print(-b)
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)
#print(a%b)
#print(a**b)

#n = int(input("Enter number:"))
#a = 0
#b = 1
#for i in range(n):
#    print(a, end=" ")
#    c = a + b
#    a = b
#    b = c

#n = int(input("Enter length of array"))
#arr = []
#print("Enter your array elements:")
#for i in range(n):
#    a = int(input())
#    arr.append(a)
#maximum = arr[0]
#for i in arr:
#    if i>maximum:
#        maximum=i
#print(f"Maximum in the array is {maximum}")

#n = int(input("Enter number of names you want to enter"))
#names = []
#print = ("Enter the names")
#for i in range(n):
#    nme=input()
#    names.append(nme)
#names.sort()
#print(f"Sorted names list{names}")

#def arraysum(arr):
#    sum_=0
#    for i in arr:
#        sum_+=i
#    return sum_
#n = int(input("Enter no. of elements:"))
#arr = []
#print("Enter numbers:")
#for i in range(n):
#    arr.append(int(input()))
#    sum_=arraysum(arr)
#    print("Sum of entire array:",sum_)

text = input("Enter content which you want to store in file:")
with open("file.txt","w")as f:
    f.write(text)
    print("Entered content written to the file successfully!!!")
    print("File closed")
with open("file.txt","r")as f:
    file_text  = f.read()
    print("content pf file:\n",file_text)