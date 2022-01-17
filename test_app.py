from app import app
import pytest

currency = ["USD", "EUR", "INR", "GBP", "JPY"]
def test_app():
    for item in currency:
        response = app.test_client().get("/{}".format(item))
    # response = app.test_client().get('/')
        assert response.status_code == 200

def test_type_error():
    response = app.test_client().get("/abc")
    assert response.status_code == 500
    # with pytest.raises(TypeError):
    #     app.test_client().get("/abc")

# def test_zero():
#     with pytest.raises(ZeroDivisionError):
#         1 / 0