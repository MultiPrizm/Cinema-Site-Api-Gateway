from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import MinValueValidator, MaxValueValidator
from InfoCenter.models import Sessions
import uuid

class Users(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.TextField(max_length=50)
    last_name = models.TextField(max_length=50)
    password = models.TextField(max_length=150)
    gmail = models.TextField(max_length=100)
    phone_number = models.TextField(max_length=100)

    def save(self, *args, **kwargs):

        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

class Reservations(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    sessions_id = models.ForeignKey(Sessions, on_delete=models.CASCADE)
    number_place = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])