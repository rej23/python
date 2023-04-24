word = input("enter a word: ")
wcount = 0
counter = 0

while counter < len(word):
    x = word[counter]
    if x.lower() in "aeiou":
        wcount += 1
    counter += 1 

print("word = ", word ," vowel count = ",wcount)