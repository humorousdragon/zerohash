from app import app
import pytest

currency = ["USD", "EUR", "inr", "GBP", "JPY"]

## Function to test response by passing currency from list
def test_app():
    for item in currency:
        response = app.test_client().get("/{}".format(item))
    # response = app.test_client().get('/')
        assert response.status_code == 200

## Function to test response code to be 500 when passing random input e.g. abc
def test_type_error():
    response = app.test_client().get("/abc")
    assert response.status_code != 200
    # with pytest.raises(TypeError):
    #     app.test_client().get("/abc")

## Test to check if response type is json or not with currency endpoint
def test_json():
    response = app.test_client().get("/USD")
    assert response.content_type == "application/json"

# def test_zero():
#     with pytest.raises(ZeroDivisionError):
#         1 / 0