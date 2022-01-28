from django.urls import path

from library.views import (
    add_author_view,
    add_book_view,
    books_list_view,
    borrow_book_view,
    delete_author_view,
    delete_book_view,
)

app_name = "library"

urlpatterns = [
    path("", books_list_view, name="book-list"),
    path("add-book/", add_book_view, name="add-book"),
    path("delete-book/<uuid:id>/", delete_book_view, name="delete-book"),
    path("borrow-book/<uuid:id>/", borrow_book_view, name="borrow-book"),
    path("add-author/", add_author_view, name="add-author"),
    path("delete-author/<uuid:id>/", delete_author_view, name="delete-author"),
]
