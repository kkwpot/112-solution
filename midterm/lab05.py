# Lab 05 Problem

# 01: Digits

x = int(input())
if x <= 0:
    print("ERROR")
else:
    while True:
        if x/10 == 0:
            break
        print(x - (x//10)*10)
        x = x//10

# 02: Harder Parking

if hours < 0 or hours > 20 or minutes < 0 or minutes > 59:
    print("Invalid time.")
elif hours == 20 and minutes > 0:
    print("Invalid time.")
else:    
    if minutes != 0:
        hours = hours + 1
    
    
    if (buyAmt >= 3001):
        print("No charge, thank you.")
    elif (buyAmt >= 300):
        if (hours <= 4):
            print("No charge, thank you.")
        elif (hours > 4):
            print(f"Total amount due is {(hours-4)*50} Baht, thank you.")     
    else:
        if (hours <= 2):
            print("No charge, thank you.")
        elif (hours <= 4):
            print(f"Total amount due is {(hours-2)*20} Baht, thank you.")
        elif (hours > 4):
            print(f"Total amount due is {40+(hours-4)*50} Baht, thank you.")  
        
# 03: Count Positive Odd Number

count = 0
while True:
    x = int(input("Enter number: "))
    if x < 0:
        break
    if x % 2 != 0:
        count = count + 1
print(f"Received {count} odd numbers")

# 04: Multiple Lines Star Pattern

num = int(input())
char = input()
i = 1
while i <= num:
    print(char*i)
    i = i+1
    
# 05: Triangle of 1s

i = 1
num = int(input("Enter height: "))
while True:
    if (i > num):
        break
    if (i == 1):
        print(' '*(2*(num-i)) + '1')
    else:
        print(' '*(2*(num-i)) + '1' + ' '*(4*i-5) + '1')
    i = i+1
    
# 06: Rule of Nine

x = int(input())
summ = 0

while True:
    if x/10 == 0:
        break
    summ = summ + (x - (x//10)*10)
    x = x//10

if summ%9 == 0:
    print(f"Yes {summ}")
else:
    print(f"No {summ%9}")
