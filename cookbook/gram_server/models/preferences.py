from django.contrib.auth.models import User
from django.db import models
from cookbook.gram_server.models import Crops


class UserCropPreferences(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    crop = models.ForeignKey(Crops, on_delete=models.CASCADE)
    preference_order = models.IntegerField(default=0)

    class Meta:
        unique_together = ['user', 'crop']
