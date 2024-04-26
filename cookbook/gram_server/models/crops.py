from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _


class Crops(models.Model):
    crop_id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="ID")
    crop_name_hi = models.CharField(
                max_length=100,
                help_text=_("Crop Name Hindi"),
            )
    crop_name = models.CharField(help_text=_("Crop Name."), max_length=80)
    image_thumbnail = models.CharField(help_text=_("image thumbnail."), max_length=255)
