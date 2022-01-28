from django.db import models
import uuid


class BaseModel(models.Model):
    """
    Model abstraction to share common model properties in database
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
