import graphene

from cookbook.gram_server.models import UserCropPreferences
from .types import CropPreferenceInput


class SetUserPreferences(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        input = graphene.List(CropPreferenceInput)

    def mutate(self, info, **data):
        user = info.context.user
        try:
            UserCropPreferences.objects.filter(user=user).delete()
            for preference in data.get('input', {}):
                crop_id = preference.get('crop_id')
                preference_order = preference.get('preference_order')
                UserCropPreferences.objects.create(user=user, crop_id=crop_id, preference_order=preference_order)
        except Exception:
            return SetUserPreferences(success=False)

        return SetUserPreferences(success=True)

