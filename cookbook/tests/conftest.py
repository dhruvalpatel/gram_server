import pytest
from cookbook.schema import schema
from graphene.test import Client as GraphqlClient
from .factories import UserFactory
from snapshottest.pytest import PyTestSnapshotTest
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from .factories import CropsFactory
import uuid

@pytest.fixture
def request_headers():
    """Return the context dict"""

    def fn(user: User = AnonymousUser()) -> dict:
        context = type("", (), {})()
        if not user.is_anonymous:
            user.access_token = "hello"
        context.user = user
        context.access_token = "hello"
        return context

    return fn

def assert_no_error(response: dict) -> None:
    """Asset there is no errors key in response."""
    assert not response.get("errors", [])


def clear_ignore_keys(data, ignore_keys=["id"]):
    """Return dict by removing keys."""
    if isinstance(data, dict):
        data = {
            key: clear_ignore_keys(value, ignore_keys)
            for key, value in data.items()
            if key not in ignore_keys
        }
    elif isinstance(data, list):
        data = [clear_ignore_keys(item, ignore_keys) for item in data if item not in ignore_keys]
    return data


class CustomPyTestSnapshotTest(PyTestSnapshotTest):
    """Custom Pytest class for skipping keys while assert."""

    def assert_match(self, data, ignore_keys=["id"]):
        if ignore_keys:
            data = clear_ignore_keys(data, ignore_keys)

        super(CustomPyTestSnapshotTest, self).assert_match(data)


@pytest.fixture(scope="function")
def user():
    user = UserFactory.create(
        username='dhruval',
        email='dhruval@gmail.com',
        password='pass'
    )
    return user


@pytest.fixture(scope="function")
def user_graphql_client(request_headers, user):
    """Get graphql client for user."""
    return GraphqlClient(schema, context_value=request_headers(user))


@pytest.fixture
def snapshot(request):
    with CustomPyTestSnapshotTest(request) as snapshot_test:
        yield snapshot_test


@pytest.fixture
def crops():
    crops_data = [
        {"crop_name": "Wheat", "crop_name_hi": "ghenhu", "image_thumbnail": "wheat.jpg"}
    ]

    for crop in crops_data:
        CropsFactory.create(
            crop_id=uuid.uuid4(),
            crop_name=crop['crop_name'],
            crop_name_hi=crop['crop_name_hi'],
            image_thumbnail=crop['image_thumbnail']
        )
