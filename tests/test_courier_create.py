from typing import Any, Literal
import pytest
import allure
from methods import courier
from data import MSG
from helpers import DataGenerator 


@allure.feature("Создание курьера")
class TestCreateCourier:
    
    @allure.title("Успешное создание курьера")
    def test_create_courier_success_shows_ok_true(self):
        courier_data = DataGenerator.generate_courier_data()
        
        with allure.step("Создаем нового курьера"):
            response = courier.create_courier(courier_data)
        
        assert response.status_code == 201, \
            f"Ожидался код ответа 201 (Created), получен {response.status_code}"
        
        assert response.json() == {"ok": True}, \
            f"Ожидался ответ {{'ok': True}}, получен {response.json()}"
        
    
    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_shows_error(self, create_and_delete_courier: tuple[dict[str, str], Any]):
        courier_data, courier_id = create_and_delete_courier
        
        with allure.step("Попытка создания дубликата"):
            response = courier.create_courier(courier_data)
            
        assert response.status_code == 409, \
            f"Ожидался код ответа 409, получен {response.status_code}"
        
        assert response.json()["message"] == MSG['COURIER_DUPLICATE_LOGIN'], \
            f"Неверное сообщение об ошибке: {response.json()['message']}"
    
    @allure.title("Создание курьера без обязательных полей")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_create_courier_missing_field_shows_error(self, missing_field: Literal['login'] | Literal['password']):
        courier_data = DataGenerator.generate_courier_data()
        del courier_data[missing_field]
        
        with allure.step(f"Создание курьера без поля {missing_field}"):
            response = courier.create_courier(courier_data)
            
        assert response.status_code == 400, \
            f"Ожидался код ответа 400, получен {response.status_code}"
        
        assert response.json()["message"] == MSG['COURIER_CREATE_NO_DATA'], \
            f"Неверное сообщение об ошибке: {response.json()['message']}"
    
    @allure.title("Создание курьера с существующим логином")
    def test_create_courier_with_existing_login(self, create_and_delete_courier: tuple[dict[str, str], Any]):
        courier_data, courier_id = create_and_delete_courier
        
        with allure.step("Попытка создания курьера с существующим логином"):
            response = courier.create_courier({
                "login": courier_data["login"],
                "password": DataGenerator.generate_random_string(10),
                "firstName": DataGenerator.generate_random_string(10)
            })
            
        assert response.status_code == 409, \
            f"Ожидался код ответа 409, получен {response.status_code}"
        
        assert response.json()["message"] == MSG['COURIER_DUPLICATE_LOGIN'], \
            f"Неверное сообщение об ошибке: {response.json()['message']}"