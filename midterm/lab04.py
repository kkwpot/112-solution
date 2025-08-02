# Lab 04 Problem

# 01: Guessing 2

x = float(input("Enter your guess (0 - 100): "))

if ((x < 0) or (x > 100)):
    print("Sorry, out of range, try again later.")
elif x == target:
    print("Congratulations, your guess is correct.")
elif x < target:
    print("Sorry, your guess is too low, try again later.")
else:
    print("Sorry, your guess is too high, try again later.")

# 02: Menu

error = False
errorY = False

print("""---<< Main Menu >>---
    <B>urger Meal
    <C>hicken Meal
    <P>asta Meal""")

x = input("Enter your choice: ")
x = x.upper()
if (x == 'B'):
    print("""---<< Burger Sub Menu >>---
    <R>egular Burger
    <C>heese Burger
    <D>ouble Cheese Burger""")
elif (x == 'C'):
    print("""---<< Chicken Sub Menu >>---
    <F>ried Chicken
    <G>rilled Chicken
    <C>hef's Chicken""")
elif (x == 'P'):
    print("""---<< Pasta Sub Menu >>---
    <S>paghetti de Italiano
    <L>asagna Supreme
    <M>acaroni Special""")
else:
    error = True
    
if error == True:
    print("Invalid main menu choice.")
    errorY == True
else:
    
    y = input("Enter your choice: ")
    y = y.upper()
    if (x == 'B'):
        if (y == 'R'):
            food = "Regular Burger"
            cost = 60
        elif (y == 'C'):
            food = "Cheese Burger"
            cost = 75
        elif (y == 'D'):
            food = "Double Cheese Burger"
            cost = 90
        else:
            errorY = True
            
    elif (x == 'C'):
        if (y == 'F'):
            food = "Fried Chicken"
            cost = 120
        elif (y == 'G'):
            food = "Grilled Chicken"
            cost = 150
        elif (y == 'C'):
            food = "Chef's Chicken"
            cost = 180
        else:
            errorY = True
            
    else:
        if (y == 'S'):
            food = "Spaghetti de Italiano"
            cost = 90
        elif (y == 'L'):
            food = "Lasagna Supreme"
            cost = 120
        elif (y == 'M'):
            food = "Macaroni Special"
            cost = 100
        else:
            errorY = True
# output
if error == False:
    if errorY == True:
        print("Invalid sub menu choice.")
    else:
        print(f"Your {food} is {cost} Baht.")

# 03: Electric Appliance Store

tv = int(input("How many TVs? "))
dvd = int(input("How many DVD players? "))
audio = int(input("How many Audio Systems? "))

total = tv*6000 + dvd*1500 + audio*3000
print(f"Total price is {total:.2f} baht.")


if (total >= 24000):
    print(f"You've got a discount of {total*2/10:.2f} baht.")
    total = total*8/10

print(f"Your payment is {total:.2f} baht. Thank you!")

# 04: Buffet

error = False

buffet = input("Enter your buffet choice: ")

if (buffet == "Japanese"):
    baht = 1000
elif (buffet == "Korean"):
    baht = 1500
else:
    print(f"Sorry, there is no {buffet} buffet.")
    error = True
    
if not error:
    wednesday = input("Is today Wednesday (yes/no)? ")
    if wednesday == "yes":
        baht = baht*85/100
    print(f"Your payment is {baht:.2f} Baht.")    

# 05: NIT

age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))

if (age < 15) or (age > 60):
    print("Invalid age.")
elif (income < 0) or (income >= 80000):
    print("Invalid income.")
elif (income <= 30000):
    got = income*20/100
    print(f"Your negative income tax is {got:.2f} Baht.")
elif (income <= 79999):
    got = (80000-income)*12/100
    print(f"Your negative income tax is {got:.2f} Baht.")
    
# 06: Leap Year

year = int(input("Enter year: "))

if (year <= 0):
    print(f"Invalid year.")
elif (year%4 == 0) and (year%100 != 0) or (year%400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# 07: Pokemon

lvlPokemon = float(input("Enter level pokemon: "))
b = input("Enter level pokeball: ")
d = float(input("Enter distance: "))

if (b == 'h') or (b == 'H'):
    x = 0.01
elif (b == 'm') or (b == 'M'):
    if (lvlPokemon <= 40):
        x = 0.03
    elif (lvlPokemon <= 60):
        x = 0.05
    elif (lvlPokemon <= 100):
        x = 0.08
elif (b == 'l') or (b == 'L'):
    if (lvlPokemon <= 40):
            x = 0.05
    elif (lvlPokemon <= 60):
            x = 0.03	
    elif (lvlPokemon <= 100):
            x = 0.1

s = 100 - (lvlPokemon*d*x)

if s < 0:
    s = 0
print(f"{s:.2f} percent.")

# 08: Homework

import math

m = int(input("Minutes before due: "))
temp = float(input("Temperature: "))
rain = input("Is it raining (y/n)? ")

if (rain == 'y' or rain == 'Y'):
    rain = True
else:
    rain = False

day = m // 1440
if m % 1440 >=720:
    day = day+1

if day < 2:
    do = True
elif day > 5:
    do = False
elif (temp > 40) or ((temp > 25) and rain):
    do = False
else:
    do = True
    
print(f">>> {day} days before due.")
if do:
    print(">>> I will do the assignment.")
else:
    print(">>> I will not do the assignment.")
