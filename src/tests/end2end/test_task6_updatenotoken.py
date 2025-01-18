import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.helpers.api_requests_wrapper import *
from src.utilis.utilis import Utilis

class Testupdatentoken(object):

    @allure.title("Update booking id without token")
    @allure.description("Verify whether we are able to update the booking id without passing token or not")
    def testupdatenotoken(self,get_booking_id):
        booking_id=get_booking_id

        update_url=APIConstants.url_patch_put_delete(booking_id=booking_id)

        response_update=put_request(
            url=update_url,
            auth=None,
            headers=Utilis().common_header_put_delete_patch_cookie(token=None),
            payload=payload_update_booking(),
            in_json=False
        )

        assert response_update.status_code==403