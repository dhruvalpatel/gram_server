import pytest
from cookbook.tests.conftest import assert_no_error

GQL = """
query meQuery {
  me {
    username
    email
  }
}
    """


@pytest.mark.django_db(reset_sequences=True)
def test_me_query(
    user_graphql_client,
    snapshot,
    user,
):
    """Test get user."""

    response = user_graphql_client.execute(GQL)

    assert_no_error(response)
    snapshot.assert_match(response)
