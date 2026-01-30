import pytest
from helpers import DataGenerator
from methods import ScooterMethods


@pytest.fixture(scope="function")
def create_and_delete_courier():
    courier = ScooterMethods()
    courier_data = DataGenerator.generate_courier_data()
    response = courier.create_courier(courier_data)
    courier_id = courier.login_courier(courier_data["login"], courier_data["password"]).json()["id"]
    yield courier_data, courier_id
    courier.delete_courier(courier_id)


@pytest.fixture(scope="function")
def create_and_cancel_order():
    order = ScooterMethods()
    order_data = DataGenerator.generate_order_data()
    response = order.create_order(order_data)
    track = response.json()["track"]
    
    yield order_data, track
    order.cancel_order(track)


@pytest.fixture(scope="function")
def courier_data():
    courier = ScooterMethods()
    courier_data = DataGenerator.generate_courier_data()
    yield courier_data
    login_response = courier.login_courier(
        courier_data["login"],
        courier_data["password"]
        )
    courier_id = login_response.json().get("id")
    if courier_id:
        courier.delete_courier(courier_id)