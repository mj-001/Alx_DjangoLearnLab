
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from django.contrib.auth import login
from .forms import BookForm

from .models import Book
from .models import Library

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'


# User Login View (built-in)
class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# User logout View (built-in)
class UserLogoutView(LogoutView):
    template_name = 'relationship_app/login.html'


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

# Admin View
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')


# Librarian View
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')


# Member View
@user_passes_test(is_member)
def member_view(request):
    return render(request,'member_view.html')


# Add Book View
@permission_required('books.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})


# Edit Book View
@permission_required('books.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.id)
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})


# Delete Book View
@permission_required('books.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'delete_book.html', {'book': book})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('login')  # Redirect to login page
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Use Django's built-in views for login and logout
class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Helper function to check user role
def user_is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def user_is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def user_is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@login_required
@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'member_view.html')
