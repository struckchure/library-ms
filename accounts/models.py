from django.db import models
from django.contrib.auth.models import AbstractUser

from library_ms.utils import BaseModel


class User(BaseModel, AbstractUser):

    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    def borrow_book(self, book):
        # import Borrow model here to avoid circular import error
        from library.models import Borrow

        borrow = Borrow.objects.create(user_id=self.id, book=book)
        borrow.save()

        return borrow
