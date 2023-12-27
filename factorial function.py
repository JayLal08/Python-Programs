def fact():

  a = int(input("Enter a number"))
  fact = 1
  i = 1
  while(i<a+1):
    fact = fact * i
    i = i + 1
    print(fact)
fact()