# Generated by Django 5.0.4 on 2024-04-25 10:13

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram_server', '0002_add_preference_table'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salereceipt',
            name='user_id',
        ),
        migrations.AddField(
            model_name='salereceipt',
            name='price_updated',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='prices_updated'),
        ),
        migrations.AddField(
            model_name='salereceipt',
            name='user',
            field=models.ForeignKey(default=3, help_text='User Id.', on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
