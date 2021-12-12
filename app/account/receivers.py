import re

from account.models import User

from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def user_pre_save_email_field(sender, instance, **kwargs):
    if instance.email:
        instance.email = instance.email.lower()


@receiver(pre_save, sender=User)
def user_pre_save_phone_field(sender, instance, **kwargs):
    if instance.phone:
        instance.phone = re.sub('[^0-9]', '', instance.phone)

# @receiver(post_save, sender=User)
# def user_post_save(sender, instance, **kwargs):
#     print('post_save')
