# Retrieve Operation
Command:

book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)

# Expected Output:
1984 George Orwell 1949

book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
