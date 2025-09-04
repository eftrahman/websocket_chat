from django.contrib.auth.models AbstractUser
from django.db import models

class CustomUser(AbstractUser)
    def __str__(self):
        return self.username
