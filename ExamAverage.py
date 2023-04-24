
mark1 = 0
mark2 = 0
mark3 = 0

while (mark1 < 0 or mark1 >100):
    mark1 = int(input("input a mark from 0-100: "))
while (mark2 < 0 or mark2 >100):
    mark2 = int(input("input a mark from 0-100: "))
while (mark3 < 0 or mark3 >100):
    mark3 = int(input("input a mark from 0-100: "))

average_mark = (mark1 + mark2 + mark3) / 3

if average_mark >= 65:
    result = "pass"
else:
    result = "fail"

print("average mark = ", average_mark , "result = ", result)