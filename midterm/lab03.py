# Lab 03 Problem

# 01: BMI

w = float(input("Weight (kg): "))
h = float(input("Height (m): "))
bmi = w/(h*h)
print(f"BMI is {bmi:.1f}")
if (bmi < 18.5):
    print("Underweight")
elif (bmi < 25 ):
    print("Normal weight")
elif (bmi < 30):
    print("Overweight")
else:
    print("Obesity")

# 02: ACME

cost = float(input("Enter buying amount: "))

if (cost >= 1000) and (cost < 3000):
    discount = cost * 0.9
elif (cost >= 3000):
    discount = cost * 0.85
else:
    discount = cost

print(f"Amount due after discount is {discount:.2f} baht.")

# 03: Parking

h = float(input("Enter number of hours: "))
m = float(input("Enter number of minutes: "))

if ((h >= 0) and (m >= 0) and (m < 60)):
    
    if (m <= 15 and h == 0):
        print("No charge, thanks.")
    elif (h*60+m <= 120):
        print("Total amount due is 10 Bahts.")
    else:
        if m == 0:
            h = h-1
        print(f"Total amount due is {h*10:.0f} Bahts.")
        
else:
    print("Input Error!")

# 04: Stamp

p = float(input("Total Price: "))
print(f"You got: {int(p//50)}")

# 05: Guessing 1

guess = int(input("Enter your guess (0 - 100): "))
if (guess >= 0) and (guess <= 100):
    if target == guess:
        print("Congratulations, your guess is correct.")
    else:
        print("Sorry, your guess is wrong, try again later.")
else:
    print("Sorry, out of range, try again later.")

# 06: Admin Account

un = input("Username: ")
pw = input("Password: ")

if (un == ADMIN_USERNAME) and (pw == ADMIN_PASSWORD):
    print("Welcome, admin.")
else:
    print("You are not admin.")

# 07: Calculate f(x)

import math

x = float(input("Enter x : "))

if (x < 0):
    y = math.sqrt(x*x+1)
elif (x == 0):
    y = x
elif (x <= 99):
    y = 3*x*x - (1-x)*(1-x)
else:
    y = 2*x*x*x - (x/(math.sqrt(x+1)))

print(f"f({x:.2f}) = {math.ceil(y)}")
