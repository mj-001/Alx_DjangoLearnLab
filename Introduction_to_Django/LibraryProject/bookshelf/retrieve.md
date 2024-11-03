# Retrieve the Book instance

```python
# Retrieving the book we just created
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
1984 George Orwell 1949