from django.db import models
import uuid

class Films(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    genre = models.TextField()
    description = models.TextField()
    rating = models.TextField()

class Sessions(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)