from email.policy import default
import os
import uuid
from io import BytesIO

from PIL import Image
from django.core.files import File
from django.db import models
from django.utils import timezone
from rest_framework.test import APIClient

client = APIClient()


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"{now:%Y%m%d%H%M%S}{milliseconds}{extension}"


# image compression method
def compress(image):
    im = Image.open(image)
    img_converted=im.convert("RGB")
    im_io = BytesIO()
    img_converted.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image


# Create your models here.
class Images(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to=upload_to, default="profile.png")
    model = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'tbl_images'
        ordering = ('created_at',)

    def __str__(self):
        return str(self.image)

    def save(self, *args, **kwargs):
        try:
            Image.open(self.image)
            new_image = compress(self.image)
            self.image = new_image
        except:
            print("none")
        super().save(*args, **kwargs)
