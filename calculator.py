#weight = input("your weight")

print("option")
print("1 = +")
print("2 = -")
print("3 = x")
print("4 = /")

n1 = float(input("first number:"))
n2 = float(input("second number: "))


option = input("input option mumber:")

if option == "1":
    o = n1 + n2
    print(o)
elif option == "2":
    o = n1 - n2
    print(o)
elif option == "3":
    o = n1 * n2
    print(o)
elif option == "4":
    o = n1 / n2
    print(o)
else:
    print("pick from 1 to 4")

    

    