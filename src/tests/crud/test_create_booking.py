import pytest
import allure
import logging # THis is use to print the message- Logs

from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *  # import all the verification
from src.utilis.utilis import Utilis

class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that create booking status and booking ID shouldn't be null")
    @allure.description("Creating Booking from te payload and verify that booking ID should not be equal to null")
    def test_create_booking_positive(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the Testcase of TestCreateBooking")
        LOGGER.info("POST Req Started.")
        response=post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utilis().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        LOGGER.info("POST Req Done.")
        LOGGER.info("Now Verify")
        verify_http_status_code(response_data=response,expected_data=200)
        LOGGER.info(response.json())
        LOGGER.info(response.json()["bookingid"])
        verify_json_key_not_null(response.json()["bookingid"])
        verify_json_key_gr_zero(response.json()["bookingid"])


    @pytest.mark.negative
    @allure.title("Verify that Create Booking with invalid payload")
    @allure.description("Creating a Booking id invalid, verify 500 for the correct payload")

    def test_create_booking_negative_tc1(self):
        LOGGER=logging.getLogger(__name__)
        LOGGER.info("Starting the testcase of invalid payload")

        response=post_request(url=APIConstants().url_create_booking(),
                              auth=None,
                              headers=Utilis().common_headers_json(),
                              payload={},
                              in_json=False
                              )

        verify_http_status_code(response_data=response,expected_data=500)


    @pytest.mark.negative
    @allure.title("Verify that Create Booking with invalid payload Part 2")
    @allure.description("Creating a Booking id invalid, verify 500 for the incorrect payload")
    def test_create_booking_negative_tc2(self):

        LOGGER=logging.getLogger(__name__)
        LOGGER.info("Starting the Testcase of invalid request")
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utilis().common_headers_json(),
            payload={"name":"Gajendran"},
            in_json=False

        )
        verify_http_status_code(response_data=response,expected_data=500)

