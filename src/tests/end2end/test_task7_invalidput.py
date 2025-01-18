import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.helpers.common_verification import *
from src.helpers.api_requests_wrapper import *
from src.utilis.utilis import Utilis

class Testinvalidput(object):

    @allure.title("Invalid put request")
    @allure.description("Verify whether we are able to update the booking by invalid put request")
    def testinvalidputrequest(self,create_token,get_booking_id):

        booking_id=get_booking_id
        token=create_token

        update_url=APIConstants.url_patch_put_delete(booking_id=booking_id)

        response_update=put_request(
            url=update_url,
            auth=None,
            headers=Utilis().common_header_put_delete_patch_cookie(token=token),
            payload={"firstname":"Raj"},
            in_json=False
        )

        assert response_update.status_code==400
        print(response_update.status_code)