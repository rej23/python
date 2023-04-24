    
print("1.Find the length of A given B and C  ")
print("2.Find the length of B given A and C ")
print("3.Find the length of C given A and B ")

a = input("Enter option 1,2 OR 3: ")

if a == "1":
    side_b = float(input("length of side B = "))
    side_c = float(input("length of side C = "))
    side_a = (side_c**2 - side_b**2)**0.5
    print("Lenght for A =", side_a)
elif a == "2":
    side_a = float(input("length of side A = "))
    side_c = float(input("length of side C = "))
    side_b = (side_c**2 - side_a**2)**0.5
    print("length of side B =", side_b)
elif a == "3":
    side_a = float(input("length of side A = "))
    side_b = float(input("length of side B = "))
    side_c = (side_a**2 + side_b**2)**0.5
    print("length of side c =", side_c)
else:
    print("erro enter 1, 2, or 3.")