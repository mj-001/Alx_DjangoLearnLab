# Delete the book instance
book.delete()

# Attempt to retrieve all books to confirm deletion
Book.objects.all()
# Expected output:
# <QuerySet []>
