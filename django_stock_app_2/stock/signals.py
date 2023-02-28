from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Purchases, Sales

@receiver(pre_save, sender = Purchases)
def colcature_price_total(sender, instance, **kwargs):
    instance.price_total = instance.quantity * instance.price

@receiver(pre_save, sender = Sales)
def colcature_price_total(sender, instance, **kwargs):
    instance.price_total = instance.quantity * instance.price