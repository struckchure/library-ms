from django.db import models
from django.utils import timezone

from accounts.models import User
from library_ms.utils import BaseModel


class Author(BaseModel):

    full_name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.full_name


class Book(BaseModel):

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    cover = models.ImageField()
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    publication_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.title} - {self.author.full_name}"


class Borrow(BaseModel):

    # default borrow duration is 14 days / 1 week
    # if the default duration should be changed, re-run db migrations

    BORROW_DURATION = timezone.timedelta(weeks=1)

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    has_returned = models.BooleanField(default=False)
    borrow_duration = models.DurationField(default=BORROW_DURATION)

    def __str__(self):
        return self.user.username

    @property
    def return_date(self):
        return self.created + self.borrow_duration
