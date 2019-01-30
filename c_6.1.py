# deriving the power of number using function and without using return statement #

def pow(a,b):
    print("The value of a^b is: ",a**b)

a=int(input("Enter the first value: "))
b=int(input("Enter the second value: "))
pow(a,b)

# deriving the power of number using function and with using return statement #

def pow(a,b):
    c=a**b
    return(c)

a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
c=pow(a,b)
print("The value of a^b is: ",c)