key = 8
a = [2,5,8,9,12,2]

for i in a:

 if(i == key):
        print("Element found")
else:
    print("Element is not found") 

key = 50
a = [2,5,8,9,12,2]
s=0
for i in a:
    if(i == key):
        s=1
        break 
if(s == 1):
        print("Element found")
else :
    print("Element not found")