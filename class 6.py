# Area of circle using function and without return statement #

pi = 3.1415
def cir(r):
    print("The area of circle is: ",pi*r*r)

x = float(input("Enter the value of radius: "))
cir(x)

# Area of circle using function and with return statement #

pi = 3.1415
def cir(r):
    s=pi*r*r
    return(s)

x = float(input("Enter the value of radius: "))
s=pi*x*x
print("The area of circle is: ",s)
