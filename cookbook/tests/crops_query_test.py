import pytest
from cookbook.tests.conftest import assert_no_error


GQL = """
query crops {
  crops(ascending: true) {
    cropId
    cropName
    cropNameHi
    imageThumbnail
    quantity
    receipts
    priceUpdated
    crops {
      quantity
      receiptDate
      priceUpdated
    }
  }
}
    """


@pytest.mark.django_db(reset_sequences=True)
def test_crops_query(
    user_graphql_client,
    snapshot,
    user,
    crops
):
    """Test Crops Query."""

    response = user_graphql_client.execute(GQL)

    assert_no_error(response)
    snapshot.assert_match(response, ignore_keys=["cropId","priceUpdated"])
