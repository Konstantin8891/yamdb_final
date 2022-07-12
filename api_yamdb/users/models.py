from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class CustomUser(AbstractUser):
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'

    ROLE_CHOICES = (
        (USER, 'user'),
        (MODERATOR, 'moderator'),
        (ADMIN, 'admin')
    )

    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name='email address'
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        # Валидаторы здесь, потому что у меня два разных сериализатора
        # для разных эндпоинтов, ошибки валидации хорошо видно, пример postman:
        # "username": [
        #     "This value may contain only letters,\n
        #      digits and @/./+/-/_ characters."
        # ]
        validators=[
            RegexValidator(
                regex=r'^[\w.@+-_]+$',
                message="""This value may contain only letters,
                digits and @/./+/-/_ characters."""
            ),
            RegexValidator(
                regex=r'^\b(m|M)e\b',
                inverse_match=True,
                message="""Username Me registration not allowed."""
            )
        ],
    )
    first_name = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=150,
        blank=True,
        null=True
    )
    bio = models.TextField(
        blank=True,
        null=True
    )
    role = models.CharField(
        max_length=100,
        choices=ROLE_CHOICES,
        blank=True,
        null=True,
        default=USER
    )

    def __str__(self) -> str:
        return self.username

    def is_moder(self):
        return self.role == self.MODERATOR

    def is_admin(self):
        return self.role == self.ADMIN

    def is_moder_or_admin(self):
        return self.role == self.MODERATOR or self.role == self.ADMIN

    def is_user(self):
        return self.role == self.USER
