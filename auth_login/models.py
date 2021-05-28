from django.db import models

from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save




class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_Category = models.JSONField()
    def __str__(self):
        return str(self.user)
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)
    



