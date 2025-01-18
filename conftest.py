# Reason: TO resuse create token  and create booking

import pytest
import allure
from src.constants.api_constants import APIConstants
from src.helpers.common_verification import *
from src.helpers.api_requests_wrapper import *
from src.helpers.payload_manager import *
from src.utilis.utilis import Utilis


@pytest.fixture(scope="session")
def create_token():
    response=post_request(
        url=APIConstants().url_create_token(),
        headers=Utilis().common_headers_json(),
        auth=None,
        payload=payload_create_token(),
        in_json=False
    )
    verify_http_status_code(response_data=response,expected_data=200)
    verify_json_key_not_none(response.json()["token"])
    return response.json()["token"]

@pytest.fixture(scope="session")
def get_booking_id():
    response=post_request(
        url=APIConstants().url_create_booking(),
        auth=None,
        headers=Utilis().common_headers_json(),
        payload=payload_create_booking(),
        in_json=False
    )
    booking_id = response.json()["bookingid"]
    verify_http_status_code(response_data=response,expected_data=200)
    verify_json_key_not_null(booking_id)
    return booking_id

