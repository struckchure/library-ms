from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from library.models import Author, Book
from library.forms import AuthorForm, BookForm


def books_list_view(request):
    books_queryset = Book.objects.order_by("-updated")

    context = {"books": books_queryset}

    return render(request, "library/books-list.html", context)


@login_required
def add_book_view(request):
    if request.method == "POST":
        add_book_form = BookForm(request.POST, request.FILES)

        if add_book_form.is_valid():
            add_book_form.save()

            messages.success(request, "Book has been added")

            return redirect("library:add-book")
    else:
        add_book_form = BookForm()

    context = {"add_book_form": add_book_form}

    return render(request, "library/add-book.html", context)


@login_required
def delete_book_view(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()

    messages.info(request, f"{book.title} has been deleted")

    return redirect("library:book-list")


@login_required
def borrow_book_view(request, id):
    user = request.user

    book = get_object_or_404(Book, id=id)
    user.borrow_book(book)

    messages.success(request, f"You just borrowed {book.title}")

    return redirect("library:book-list")


@login_required
def add_author_view(request):
    if request.method == "POST":
        add_author_form = AuthorForm(request.POST)

        if add_author_form.is_valid():
            add_author_form.save()

            messages.success(request, "Author has been added")

            return redirect("library:add-author")
    else:
        add_author_form = AuthorForm()

    context = {"add_author_form": add_author_form}

    return render(request, "library/add-author.html", context)


@login_required
def delete_author_view(request, id):
    author = get_object_or_404(Author, id=id)
    author.delete()

    messages.info(request, f"{author.full_name} has been deleted")

    return redirect("library:book-list")
