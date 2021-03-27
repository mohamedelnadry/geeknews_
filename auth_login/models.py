from django.db import models
import os
import sys
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"users/{instance.pk}/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

class profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(_("Avatar"), upload_to=upload_to, blank=True)



