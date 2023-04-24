initial = float(input("initial investment:"))
target = float(input("Target value:"))
interest = float(input("interest rate in %:")) /100

years = 0 
while initial < target:
    initial *= (1 + interest) 
    years += 1

print("years = ", years)