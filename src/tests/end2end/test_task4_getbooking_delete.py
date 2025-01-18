import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.common_verification import *
from src.helpers.payload_manager import *
from src.helpers.api_requests_wrapper import *
from src.utilis.utilis import Utilis

class Testgetbookdelete(object):

    @allure.title("Getbooking -> Delete it -> Verify it")
    @allure.description("Verify whether we are able to delete a booking id by fetching the already created booking id and verify it is deleted")

    def test_getdeletebooking(self,create_token):


        token=create_token
        get_url=APIConstants().url_create_booking()

        response_get=get_request(
            url=get_url,
            headers=Utilis().common_headers_json(),
            in_json=False
        )

        booking_id=response_get.json()[1]["bookingid"]
        print(booking_id)

        del_url=APIConstants.url_patch_put_delete(booking_id=booking_id)

        response_delete=delete_requests(
            url=del_url,
            auth=None,
            headers=Utilis().common_header_put_delete_patch_cookie(token=token),
            in_json=False
        )

        assert response_delete.status_code==201
        get_url=APIConstants.get_booking_url(booking_id=booking_id)
        response_verify=get_request(
            url=get_url,
            headers=Utilis().common_headers_json(),
            in_json=False
        )

        assert response_verify.status_code==404
