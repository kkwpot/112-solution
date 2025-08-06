# Lab 06 Problem
    
    # 01: Master Mind
    
    x = int(input("Enter a target (4-digit integer): "))
    
    d = (x - (x//10)*10)
    x = x//10
    c = (x - (x//10)*10)
    x = x//10
    b = (x - (x//10)*10)
    x = x//10
    a = (x - (x//10)*10)
    
    x = int(input("Enter your guess (4-digit integer): "))
    
    d1 = (x - (x//10)*10)
    x = x//10
    c1 = (x - (x//10)*10)
    x = x//10
    b1 = (x - (x//10)*10)
    x = x//10
    a1 = (x - (x//10)*10)
    
    per = (int(a==a1) + int(b==b1) + int(c==c1) + int(d==d1))
    pos = (int(a==b1 or a==c1 or a==d1) + int(b==a1 or b==c1 or b==d1) + int(c==a1 or c==b1 or c==d1) + int(d==a1 or d==b1 or d==c1))
    
    if (per == 4):
        print("Congratulations, you just mastered my mind!!")
    else:
        if (per == 0):
            per = "No positions correct"
        elif (per == 1):
            per = "One position correct"
        elif (per == 2):
            per = "Two positions correct"
        elif (per == 3):
            per = "Three positions correct"
        elif (per == 4):
            per = "Four positions correct"
            
        if (pos == 0):
            pos = "no digits correct"
        elif (pos == 1):
            pos = "one digit correct"
        elif (pos == 2):
            pos = "two digits correct"
        elif (pos == 3):
            pos = "three digits correct"
        elif (pos == 4):
            pos = "four digits correct"
        print(f"{per}, {pos}")
        
    # 02: Guessing 3

    target = 72
    count = 0
    
    while True:
        x = int(input("Enter your guess: "))
        count += 1
        if x > 100 or x < 0:
            print("Sorry, your guess is out of range.")
        elif x < target:
            print("Sorry, your guess is too low.")
        elif x > target:
            print("Sorry, your guess is too high.")
        else:
            print("Congratulations, your guess is correct.")
            break
    print(f"Total number of guesses is {count}.")
    
    # 03: GCD LCM
    
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    holder = 0
    firstA = a
    firstB = b
    # gcd
    while True:
        if b == 0:
            break;
        holder = a % b
        a = b
        b = holder
        
    print(f"  >> gcd({firstA}, {firstB}) ={a:7.0f}")
    print(f"  >> lcm({firstA}, {firstB}) ={firstA*firstB/a:7.0f}")
    
    # 04: Bowling

    score = 0
    round = 1
    while True:
        if round == 11:
            break
        
        print(f"Frame # {round}")
        x = int(input("  Number of pins down: "))
        
        if x == 10:
            score += x
        else:
            score += x
            print(f"Frame # {round}")
            x = int(input(f"  Number of pins down (0-{10-x}): "))
            score += x
        round += 1
        
    print(f"Total score is {score}")
    
    # 05: Building
    
    count = 0;
    maxx = -1;
    
    while True:
        x = int(input())
        if x == -1:
            break;
        if x > maxx:
            maxx = x
            count += 1;
    
    print(count)
    
    # 06: Sum Until Digit

    x = int(input())
    summ = 0

    while True:  
        while True:
            if x/10 == 0:
                break
            summ = summ + (x - (x//10)*10)
            x = x//10
            
        if summ//10 == 0:
            break
        else:
            x = summ
            summ = 0    
            
    print(summ)
