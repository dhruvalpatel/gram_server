import factory
from django.contrib.auth.models import User
from cookbook.gram_server.models import Crops


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    is_active = True
    is_staff = False
    is_superuser = False


class CropsFactory(factory.django.DjangoModelFactory):
    """Crops model factory."""

    class Meta:
        model = Crops
