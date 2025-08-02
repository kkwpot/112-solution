import math

# Lab 02 Problem

# 01: Area and Circumference

r = float(input("Enter a radius: "))
PI = math.pi

print("Area of a circle with radius %d is %.2f" % (r,PI*r*r))
print("Circumference of a circle with radius %d is %.2f" % (r,PI*r*2))

# 02: Pool

w = float(input("Enter width: "))
l = float(input("Enter length: "))
d = float(input("Enter depth: "))

rate = (w*l*d)*15/60
print("Time to fill a pool is %.2f minutes." % (rate))

# 03: Order

ti = float(input())
e = float(input())
p = ti+e

# ...

ti = f"Total Income {ti:+8.2f} bahts"
e = f"Expense {e:13.2f} bahts"
p = f"Profit       {p:08.2f} bahts"

print(ti)
print(e)
print(p)

# 04: Fraction

print("First fraction:")
a = int(input(">>Enter a numerator a: "))
b = int(input(">>Enter a denominator b: "))
print("Second fraction:")
c = int(input(">>Enter a numerator c: "))
d = int(input(">>Enter a denominator d: "))

print("Summation of the two fractions is",a*d+c*b,"/",b*d)

# 05: Gas

d = int(input())
litre = int(input())

sum = (d/15) / (litre/100)
print(int(sum/50)+1)
print(int(sum/90)+1)

# 06: Star Pattern

num = int(input())
A = input()
B = input()

print((A+B)*(num//2) + A*(num%2))

# 07: Math Function

x = float(input("Enter x: "))
y = float(input("Enter y: "))
z = float(input("Enter z: "))

print(f"a1 = {pow(x,y) + z:.2f}")
print(f"a2 = {math.cos(2*math.pi)+math.log(x):.2f}")
print(f"a3 = {math.fabs(x)+math.fabs(y):.2f}")
print(f"a4 = {math.sqrt(x*x + y*y + z*z):.2f}")
print(f"a5 = {math.sin(x)*math.sin(x)+math.cos(x)*math.cos(x):.2f}")
print(f"a6 = {(pow(x+y,1/5)):.2f}")
print(f"a7 = {pow(math.e,x*math.log(y)):.2f}")

