import pytest
import allure
from methods import courier
from helpers import DataGenerator

@allure.feature("Создание заказа")
class TestCreateOrder:
    
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    @allure.title("Создание заказа с цветом: {color}")
    def test_create_order_with_different_colors(self, color: list[str] | list[object]):
        test_data = DataGenerator.generate_order_data()
        test_data["color"] = color
        response = courier.create_order(test_data)
        track = response.json().get("track")
        
        assert response.status_code == 201
        data = response.json()
        assert "track" in data
               
    
    @allure.title("Создание заказа без поля color")
    def test_create_order_without_color_field(self):
        test_data = DataGenerator.generate_order_data()
        test_data.pop("color", None)
        response = courier.create_order(test_data)
        track = response.json().get("track")
        assert response.status_code == 201
        assert "track" in response.json()
        
        