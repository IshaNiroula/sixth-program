# Testing armstrong nuumber #

def armstrong(a):
    s=0
    x=a

    while x != 0:
        rem = x % 10
        s = s + (rem * rem * rem)
        x = int(x / 10)

    if s == a:
        return 1
    else:
        return 0

y=int(input("Enter the number you want to check as armstrong: "))
if armstrong(y):
    print(y,"is armstrong number.")

else:
    print(y,"is not armstrong number.")