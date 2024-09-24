from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid

class Films(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(null=False, blank=False)
    genre = models.TextField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    rating = models.TextField(null=False, blank=False)

class Halls(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    rows = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(250)])
    seats_in_row = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(500)])

class Sessions(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hall_id = models.ForeignKey(Halls, on_delete=models.CASCADE)
    film_id = models.ForeignKey(Films, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=False, blank=False)
    finish_time = models.DateTimeField(null=False, blank=False)
