# Update Operation
Command:

book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

# Expected Output:
Nineteen Eighty-Four

book.delete()
books = Book.objects.all()
print(books)
