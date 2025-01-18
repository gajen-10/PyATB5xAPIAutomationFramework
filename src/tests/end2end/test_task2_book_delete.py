import pytest
import allure

from src.constants.api_constants import APIConstants
from src.helpers.common_verification import *
from src.helpers.api_requests_wrapper import *
from src.helpers.payload_manager import *
from src.utilis.utilis import Utilis

class Testdeleteverify(object):
    @allure.title("CreateBooking -> Delete it -> Update")
    @allure.description("Verify that booking id got created was deleted and if we try to search for that bookingid we should receive 404")
    def test_create_booking(self,create_token,get_booking_id):
        booking_id=get_booking_id
        token=create_token
        #del_header=Utilis.common_header_put_delete_patch_cookie(token=token)
        delete_url=APIConstants.url_patch_put_delete(booking_id=booking_id)
        get_url=APIConstants.get_booking_url(booking_id=booking_id)

        response=delete_requests(
            url=delete_url,
            headers=Utilis().common_header_put_delete_patch_cookie(token=token),
            auth=None,
            in_json=False
                                 )
        assert response.status_code==201

        #assert verify_response_delete(response=response.text)
        response_get=get_request(url=get_url,headers=Utilis().common_headers_json(),in_json=False)
      # response_get=requests.get(url=get_url,
                  #               headers=Utilis().common_headers_json())

        assert response_get.status_code==404



