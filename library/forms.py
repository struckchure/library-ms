from django import forms

from library.models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ["id"]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ["id"]
