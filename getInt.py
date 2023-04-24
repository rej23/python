minimum = 1
maximum = 100
attempts = 0

while attempts <3:
    number = int(input("input a number between 1 to 100:  "))
    if minimum <= number <= maximum:
        print("you enter a correct number") 
        break
    else:
        print("try again!")
    
    attempts += 1
if attempts == 3:
    print("None")