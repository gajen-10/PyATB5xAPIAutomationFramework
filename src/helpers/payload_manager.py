# Payloads

# Create booking payload
# update booking payload
# Auth - Token payload

from dotenv import load_dotenv
import os
def payload_create_booking():
    payload = {"firstname": "Roger",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"

    }

    return payload

def payload_update_booking():
    payload={
        "firstname": "Ravi",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    return payload

def payload_create_token():
    load_dotenv()
    payload={
        "username": os.getenv("NAME"),
        "password": os.getenv("PASSWORD")
    }

    return payload