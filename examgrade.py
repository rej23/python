a = int(input("input your mark:"))
if a > 100:
    print("error mark must be between 1 and 100")
elif a <= 0:
    print("error mark must be between 1 and 100")
elif a < 50:
    print("Fail")
elif a <= 60:
    print("Pass")
elif a <= 70:
    print("Merit")
elif a >= 71:
    print("Distinction")