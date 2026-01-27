import pytest
from helpers import DataGenerator
from methods import courier


@pytest.fixture
def create_and_delete_courier():
    courier_data = DataGenerator.generate_courier_data()
    response = courier.create_courier(courier_data)
    courier_id = courier.login_courier(courier_data["login"], courier_data["password"]).json()["id"]
    yield courier_data, courier_id
    courier.delete_courier(courier_id)


@pytest.fixture
def create_and_cancel_order:
    order_data = DataGenerator.generate_order_data()
    response = courier.create_order(order_data)
    track = response.json()["track"]
    
    yield order_data, track
    courier.cancel_order(track)