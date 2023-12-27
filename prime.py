
for a in range(1,100):
    s=0
    for i in range(2, (a//2 + 1)):
        if(a % i == 0):
            s = s + 1
            break

    if (s == 0 and a != 1):
        print(" %d" %a, end = " ")