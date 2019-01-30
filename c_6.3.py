# To check the palindrome number #

def rev(a):
    x=a
    s=0

    while x!= 0:
        rem = x % 10
        s = 10*s + rem
        x = int(x/10)

    if s == a:
        return 1

    else:
        return 0

y=int(input("Enter the number you want to check as palindrome number: "))

if rev(y):
    print(y,"is palindrome number.")

else:
    print(y,"is not a palindrome number.")


