from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

@receiver(post_save, sender=get_user_model())
def set_default_password(sender, instance, created, **kwargs):
    if created:
        default_password = "password"
        instance.set_password(default_password)
        instance.save()

