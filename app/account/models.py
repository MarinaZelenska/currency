from django.contrib.auth.models import AbstractUser
from django.db import models
from django.templatetags.static import static


def avatar_upload_to(instance, filename):
    return f'avatars/{instance.id}/{filename}'


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField('email address', blank=True, unique=True)
    avatar = models.FileField(
        upload_to=avatar_upload_to,
        default=None,
        null=True,
        blank=True,
    )

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static('/images/anon.png')
