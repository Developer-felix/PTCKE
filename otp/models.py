import datetime
import uuid

from django.db import models
# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from pytz import utc


class Otps(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    otp = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    expire_at = models.DateTimeField(auto_now=False, null=True, blank=True)
    is_otp_authenticated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = "tbl_otp"


@receiver(pre_save, sender=Otps)
def add_expiry_time(sender, instance, *args, **kwargs):
    if instance.expire_at is not None:
        if datetime.datetime.now().replace(tzinfo=utc) > (instance.expire_at.replace(tzinfo=utc)):
            instance.expire_at = datetime.datetime.now() + datetime.timedelta(minutes=5)
    else:
        instance.expire_at = datetime.datetime.now(tz=timezone.utc) + datetime.timedelta(minutes=5)
