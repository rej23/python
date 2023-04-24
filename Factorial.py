a = int(input("input a number:"))

b = 1
while a > 1:
    b *= a
    a -= 1 
print("the input number Factorial = ", b)