from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    name = models.CharField(max_length=200)
    sur_name = models.CharField(max_length=200)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name="user"
    )

    def __str__(self):
        return f"{self.name}--{self.sur_name}"
