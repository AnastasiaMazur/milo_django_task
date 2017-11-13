from datetime import datetime
import random
from django.db import models
from django.contrib.auth.models import AbstractUser


def get_random_number():
    return random.randint(1, 100)


def get_random_date():
    year = random.randint(1950, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    birth_date = datetime(year, month, day)
    return birth_date


class User(AbstractUser):
    birthday = models.DateField(default=get_random_date)
    number = models.IntegerField(default=get_random_number)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username
