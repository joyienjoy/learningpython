
try:
    number = int(input("Enter the input number:"))
    output = number / 0
    print("output is:", output)

except ZeroDivisionError:
    print("divide by zero is not allowed.....")