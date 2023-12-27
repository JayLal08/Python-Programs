def armstrong(num):
    num=int(num)
    n_temp=num
    temp=num
    r=0
    count=0
    while(temp>0):
         N=(temp%10)
         temp//=10
         count+=1
    
    while(num>0):
         N=(num%10)
         r+=N**count
         num//=10
    if(r==n_temp):
        print(f"{n_temp} is ARMSTRONG")


for i in range(100000):
    armstrong(i)