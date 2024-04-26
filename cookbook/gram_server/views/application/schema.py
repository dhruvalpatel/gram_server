import graphene
from django.contrib.auth import get_user_model
from graphql_jwt.decorators import login_required
from cookbook.gram_server.models import SaleReceipt, Crops, UserCropPreferences
from graphql_auth.schema import MeQuery, UserQuery
from cookbook.gram_server.views.user.types import UserType
from cookbook.gram_server.views.application.types import SaleReceiptType, CropsType
from .utils import get_crops_last_updated
from .mutations import SetUserPreferences
from django.db.models import Case, When, IntegerField
from itertools import chain


class Query(UserQuery, MeQuery, graphene.ObjectType):
    whoami = graphene.Field(UserType)
    users = graphene.List(UserType)
    sales_receipts = graphene.List(SaleReceiptType)
    crops = graphene.List(CropsType, ascending=graphene.Boolean())

    @login_required
    def resolve_sales_receipts(root, info):
        return SaleReceipt.objects.all().order_by("-receipt_date")

    @login_required
    def resolve_crops(root, info, **data):
        user = info.context.user
        ascending = data.get('ascending', False)
        crop_preferences = UserCropPreferences.objects.filter(user=user).order_by(
            'preference_order' if ascending else '-preference_order')

        if crop_preferences:
            crop_ids = list(crop_preferences.values_list('crop_id', flat=True))
            ordering_conditions = [When(pk=crop_id, then=pos) for pos, crop_id in enumerate(crop_ids)]
            crops_based_on_preferences = Crops.objects.filter(pk__in=crop_ids).order_by(
    Case(*ordering_conditions, default=0, output_field=IntegerField())
)
            remaining_crops = Crops.objects.exclude(crop_id__in=crop_ids)
            filtered_crops = get_crops_last_updated(remaining_crops)

            merged_queryset = list(chain(crops_based_on_preferences, filtered_crops))
            return merged_queryset
        else:
            return get_crops_last_updated(Crops.objects.all())

    @staticmethod
    def resolve_whoami(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication Failure: You must be signed in")
        return user

    @login_required
    def resolve_users(self, info):
        return get_user_model().objects.all()


class Mutation(graphene.ObjectType):
    set_preferences = SetUserPreferences.Field()
