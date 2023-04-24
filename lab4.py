books = {"abraham": ["first book", "second book"], "mary": ["first book", "second book"], "author3": ["book1","book2"]}


print ("author name: Abraham, mary, author3")
a = input ("name of author:")

print(",".join(books[a])) 