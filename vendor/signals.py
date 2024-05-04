from django.db.models.signals import post_save
from .models import Vendor,Historical_Performance
from django.dispatch import receiver

@receiver(post_save, sender=Vendor)
def create_performance(sender, instance, created, **kwargs):
    if created:
        Historical_Performance.objects.create(vendor=instance)
        
@receiver(post_save , sender=Vendor)
def save_performance(sender, instance, **kwargs):
    instance.historical_performance.save()