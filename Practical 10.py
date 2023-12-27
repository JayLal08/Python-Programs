#WAP to calculate the area of different geometrical figure(Circle, square, Rectangle, Triangle, Equvilator, isoscles, scalar)


def circle():
    r = int(input("Enter the radius :"))
    a = 3.14*r*r
    print("Area of circle = ",a)

def square():
    r = int(input("Enter the side value :"))
    s = r*r
    print("Area of square = ",s)

def rectangle():
    l = int(input("Enter the length :"))
    b = int(input("Enter the breath :"))
    e = l*b
    print("Area of rectangle = ",e)

def triangle():
    b = int(input("Enter the base :"))
    h = int(input("Enter the height :"))
    f = 1/2*b*h 
    print("Area of triangle = ",f)

def equvilator():
    f = int(input("Enter the f :"))
    b = 1.73/4*f*f
    print("Area of equvilator = ",b)

def isoscles():
    b = int(input("Enter the breath :"))
    h = int(input("Enter the height :"))
    c = 1/2*b*h
    print("Area of isoscles = ",c)

def scalar():
    a = int(input("Enter the a :"))
    b = int(input("Enter the b :"))
    c = int(input("Enter the c :"))
    s = (a+b+c)/2
    v = s*(s-a)*(s-b)*(s-c)
    print("Area of scalar = ",v)

circle()
square()
rectangle()
triangle()
equvilator()
isoscles()
scalar()