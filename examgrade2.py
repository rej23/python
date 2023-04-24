    
a = int(input("input your a:"))
b = int(input("Enter b 1 or 2:"))

if a > 100:
   print("error a must be between 1 and 100")
elif a <= 0:
   print("error a must be between 1 and 100")
elif b == 1:
    if a < 50:
        print("Fail")
    elif a <= 60:
        print("Pass")
    elif a <= 70:
        print("Merit")
    else:
        print("Distinction")
elif b == 2:
    if a < 40:
        print("Fail")
    elif a <= 50:
        print("Pass")
    elif a <= 65:
        print("Merit")
    else:
        print("Distinction")
else:
    print("enter level 1 or 2")