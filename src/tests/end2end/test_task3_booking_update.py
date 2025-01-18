import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.common_verification import *
from src.helpers.api_requests_wrapper import *
from src.helpers.payload_manager import *
from src.utilis.utilis import Utilis

class TestUpdatebooking(object):

    @allure.title("Create Booking -> Update Booking")
    @allure.description("Verify whether we are able to update the firstname after creating booking")
    def test_update_booking(self,create_token,get_booking_id):

        booking_id=get_booking_id
        token=create_token
        update_url=APIConstants.url_patch_put_delete(booking_id=booking_id)

        response_update=put_request(
            url=update_url,
            auth=None,
            headers=Utilis().common_header_put_delete_patch_cookie(token=token),
            payload=payload_update_booking(),
            in_json=False
        )

        assert response_update.json()["firstname"]=="Ravi"