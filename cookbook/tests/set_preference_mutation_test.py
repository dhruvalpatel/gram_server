import pytest
from cookbook.tests.conftest import assert_no_error
from cookbook.gram_server.models import Crops

GQL = """
mutation setPreference($input:CropPreferenceInput!){
	setPreferences(input:[$input]){
   success 
  }
}
    """


@pytest.mark.django_db(reset_sequences=True)
def test_set_preference(
    user_graphql_client,
    snapshot,
    user,
        crops
):
    """Test set preference mutation."""
    crop = Crops.objects.first()

    variables = {"input": {"cropId": str(crop.crop_id), "preferenceOrder": 1}}

    response = user_graphql_client.execute(GQL, variables=variables)

    assert_no_error(response)
    snapshot.assert_match(response)
