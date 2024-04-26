import graphene
from graphene_django import DjangoObjectType
from cookbook.gram_server.models import SaleReceipt, Crops
from ..utils import date_5_days_before
import datetime


class SaleReceiptType(DjangoObjectType):
    class Meta:
        model = SaleReceipt
        fields = "__all__"


class CropsType(DjangoObjectType):
    quantity = graphene.Float()
    receipts = graphene.Int()
    price_updated = graphene.String()

    class Meta:
        model = Crops
        fields = ("crop_id","crop_name_hi", "crop_name", "image_thumbnail", "crops")

    @staticmethod
    def resolve_quantity(parent: Crops, info: graphene.ResolveInfo) -> float:
        quantity = sum(list(parent.crops.filter(receipt_date__date__gt=date_5_days_before()).values_list('quantity', flat=True)))
        return quantity

    @staticmethod
    def resolve_receipts(parent:Crops, info: graphene.ResolveInfo) -> int:
        return len(parent.crops.filter(receipt_date__date__gt=date_5_days_before()).all())

    @staticmethod
    def resolve_price_updated(parent:Crops, info: graphene.ResolveInfo) -> datetime:
        if parent.crops.values_list('price_updated'):
            return max(parent.crops.values_list('price_updated'))[0].strftime("%Y-%m-%d %H:%M")
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


class CropPreferenceInput(graphene.InputObjectType):
    crop_id = graphene.ID()
    preference_order = graphene.Int()


