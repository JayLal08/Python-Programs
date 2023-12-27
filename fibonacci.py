n = int(input("Enter till where you want to print: "))
a = 0
b = 1
for i in range (n):
    print(f" {a} ", end="")
    c = a + b
    a = b
    b = c