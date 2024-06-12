from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)  # Connect to the built-in post_save signal
def update_quantity_on_order_confirmation(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)