from datetime import datetime, timedelta
from cookbook.gram_server.models import SaleReceipt, Crops
from django.db.models import Subquery, OuterRef


def date_5_days_before():
    """Return date which is 5 days ago."""
    current_datetime = datetime.now()
    date_5 = current_datetime - timedelta(days=5)
    return date_5


def get_crops_last_updated(queryset):
    """Sort based on price last updated."""
    return queryset.annotate(max_price_updated=Subquery(
        SaleReceipt.objects.filter(crops=OuterRef('pk')).order_by('-price_updated').values('price_updated')[
        :1])).order_by('-max_price_updated')
