# Lab 08 Problem
    
    # 01: Circle

# BOX 1
import math

def circle(r):
    return math.pi*r*r

def circumference(r):
    return 2*math.pi*r

def sphere(r):
    return (4/3)*math.pi*r*r*r

#BOX 2
float(input("Enter a radius: "))

    # 02: Digit

#BOX 1

def digit(num):
    return num - ((num//10)*10)

def tens(num):
    return num//10 - ((num//100)*10)

def hundreds(num):
    return num//100 - ((num//1000)*10)

def thousands(num):
    return num//1000 - ((num//10000)*10)

def sum_digits(num):
    return digit(num) + tens(num) + hundreds(num) + thousands(num)

    # 03: Interest

#BOX 1

def simple_interest(p, r, t):
    return p + p*(r/100)*t
def compound_interest(p, r, t):
    return p*(1+r/100)**t

p = float(input("Enter principle: "))
r = float(input("Enter interest rate: "))
t = float(input("Enter time: "))

    # 04: Time Elapsed

#BOX 1
def read_hour():
    x = int(input("Enter hour: "))
    return x

def read_minute():
    x = int(input("Enter minute: "))
    return x

def read_second():
    x = int(input("Enter second: "))
    return x

def to_seconds(h,m,s):
    return 3600*h + 60*m + s

def time_elapsed(s,f):
    sec = f-s
    h = sec//3600
    sec = sec - h*3600
    m = sec//60
    sec = sec - m*60

    result = str(h) + " hours " + str(m) + " minutes " + str(sec) + " seconds."
    return result

    # 05: Changes

#BOX 1
def change(total, bahtType):
    return total//bahtType
#BOX 2 to 8
money, 500
money - b500*500
left, 100
left, 20
left - b20*20
left, 5
left

    # 06: nth Times SQRT

import math
def sqrt_n_times(x, n):
    if n == 0:
        return x
    else:
        x = math.sqrt(x)
        return sqrt_n_times(x, n-1)
