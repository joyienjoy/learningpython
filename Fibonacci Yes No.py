# Check number is fibonacci number or not

# To take input from the user
n = int(input("Enter a number to check: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes, Its a Number in Fibonacci series")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes, Its a Number in Fibonacci series")
    else:
        print("No, Its not in Fibonacci series")