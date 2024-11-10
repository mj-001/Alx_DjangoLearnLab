# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Book, Library, UserProfile

# Function-based view for listing books
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for library details
class LibraryDetailView(LoginRequiredMixin, DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# Role-based views
def is_admin(user):
    return user.userprofile.role == 'ADMIN'

def is_librarian(user):
    return user.userprofile.role == 'LIBRARIAN'

def is_member(user):
    return user.userprofile.role == 'MEMBER'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_dashboard.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_dashboard.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_dashboard.html')

# Permission-based views for book operations
@permission_required('relationship_app.can_add_book')
def add_book(request):
    # Add book logic here
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    # Edit book logic here
    return render(request, 'relationship_app/edit_book.html')

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    # Delete book logic here
    return render(request, 'relationship_app/delete_book.html')