# Python Program to find position of n\'th multiple of a number k in Fibonacci Series
# n   0   1   2   3   4   5   6    7   8   9   10   11    12    13    14     15     16     17
# Xn  0   1   1   2   3   5   8    13  21  34  55   89    144   233   377    610    987    1597
# eg. X4 = 3 i.e Every 4th number is multiple of 3
# eg. X5 = 5 i.e. Every 5th number is multiple of 5
# eg. X6 = 8 i.e. Every 6th number is multiple of 8

def seriesPosition(k, n):
    f1 = 0
    f2 = 1
    i = 2
    while i != 0:
        f3 = f1 + f2
        f1 = f2
        f2 = f3

        if f2 % k == 0:
            return n * i

        i += 1

    return


# A number from Fibonacci Series
k = int(input("Enter any number: "))

# Multiplying Factor
n = int(input("Enter a multiplying Factor (n): "))

print("Position of nth multiple of a number in Fibonacci Series is", seriesPosition(k,n))
