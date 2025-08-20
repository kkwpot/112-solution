# Lab 06 Problem
    
    # 01: Triangle Alphabet 1

x = int(input("Enter a number: "))
i = 0

if x > 0 and x <= 26:
        while (i < x):
                j = 0
                while (j <= i):
                    print(chr(ord('A')+j), end='')
                    j += 1
                print('')
                i += 1
else:
        print("Invalid input, program terminates.")

    # 02: Triangle Alphabet 2

x = int(input("Enter a number: "))
i = x

if x > 0 and x <= 26:
        while (i > 0):
                j = 0
                while (j < i):
                    print(chr(ord('A')+j), end='')
                    j += 1
                print('')
                i -= 1
else:
        print("Invalid input, program terminates.")

    # 03: Triangle Alphabet 3

x = int(input("Enter a number: "))


if x > 0 and x <= 26:
        i = 0
        while (i < x):
                j = 0
                while (j <= i):
                    print(chr(ord('A')+j), end='')
                    j += 1
                print('')
                i += 1        
        
        
        i = x-1
        while (i > 0):
                j = 0
                while (j < i):
                    print(chr(ord('A')+j), end='')
                    j += 1
                print('')
                i -= 1
else:
        print("Invalid input, program terminates.")

    # 04: Factorial Table

x = int(input("Enter a number: "))

if x >= 0:
        print("0! = 1 = 1")
        i = 1
        while (i <= x):
                result = 1
                print(f"{i}! = ", end = '')
                j = i
                while (j > 1):
                        print(f"{j} x ", end = '')
                        result = result * j
                        j -= 1
                print(f"1 = {result}")
                i += 1
else:
        print("Invalid input, program terminates.")

    # 05: Is Prime

while True:
    x = int(input("Enter a number: "))
    if (x == 0):
        break
    elif (x <= 1):
        print("Invalid input, try again.")
    else:
        i = 2
        isPrime = True
        while (i < x):
            if (x % i == 0):
                isPrime = False
            i += 1
        if isPrime == False:
            print(f"{x} is not a prime number.")
        else:
            print(f"{x} is a prime number.")
print("End of program, goodbye.")

    # 06: Double Rectangle Stars

h = int(input("Enter height: "))
w = int(input("Enter width: "))

if (h <= 0 or w <= 0):
    print("Invalid input, program terminates.")
else:
    i = 1
    while i <= h:
        j = 1
        while j <= w:
            if (i%2):
                print('* ',end='')
            else:
                print(' *',end='')   
            j += 1
        print()
        i += 1    

    # 07: Prime Factorization

n = int(input("Enter positive integer: "))

if n <= 0:
    print("Invalid number.")
else:
    p = 2
    while p <= n:
        stillDivisible = True
        while stillDivisible:
            if (n % p) == 0:
                n = n/p
                print(p)
            else:
                stillDivisible = False
        p += 1    

    # 08: Count All Pythagorean AB

import math
n = int(input())
value = 0
maxx = n
a = 1
while a < maxx:
    b = math.sqrt(n*n - a*a)
    if (math.floor(b) == math.ceil(b)):
        value += 1
        maxx = b
    a += 1
print(value)
