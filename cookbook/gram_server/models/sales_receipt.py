from django.db import models
from cookbook.gram_server.models import Crops
from django.contrib.auth.models import User
import uuid
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now


class SaleReceipt(models.Model):
    crops = models.ForeignKey(Crops, on_delete=models.CASCADE, related_name="crops")
    receipt_id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="ID")
    mandi_id = models.IntegerField(
        default=0,
        help_text=_("Mandi Id"),
    )
    mandi_name = models.CharField(
        max_length=80,
        help_text=_("Mandi Name"),
    )
    mandi_name_hi = models.CharField(
        max_length=80,
        help_text=_("Mandi Name Hindi"),
    )
    receipt_date = models.DateTimeField(help_text=_("Timestamp at when Receipt is generated."))
    quantity = models.FloatField(help_text=_("Quantity."))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", help_text=_("User Id."), default=User.objects.filter(username="dhruvalpatel").first().id)
    booklet_number = models.CharField(help_text=_("Booklet Number."), max_length=100)
    receipt_image_url = models.URLField(help_text=_("S3 URL of receipt image."))
    is_approved = models.BooleanField(help_text=_("is receipt approved."), default=False)
    price_updated = models.DateTimeField(help_text=_("prices_updated"), default=now)
