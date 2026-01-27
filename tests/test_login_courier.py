from typing import Any
import pytest
import allure
from ..methods import courier
from ..data import MSG
from ..helpers import DataGenerator 


@allure.feature("Авторизация курьера")
class TestLoginCourier:
    
    @allure.title("Успешная авторизация курьера с полными данными")
    def test_login_courier_with_valid_credentials_returns_id(self, create_and_delete_courier: tuple[dict[str, str], Any]):
        courier_data, courier_id = create_and_delete_courier
        response = courier.login_courier(courier_data["login"], courier_data["password"])
        
        assert response.status_code == 200
        assert response.json()["id"] == courier_id
    
    @allure.title("Авторизация с неправильным паролем возвращает ошибку")
    def test_login_courier_with_wrong_password_returns_error(self, create_and_delete_courier: tuple[dict[str, str], Any]):
        courier_data, courier_id = create_and_delete_courier
        response = courier.login_courier(courier_data["login"], "wrong_password")
        
        assert response.status_code == 404
        assert response.json()["message"] == MSG['LOGIN_NOT_FOUND']
    
    @allure.title("Авторизация с неправильным логином возвращает ошибку")
    def test_login_courier_with_wrong_login_returns_error(self, create_and_delete_courier: tuple[dict[str, str], Any]):
        courier_data, courier_id = create_and_delete_courier
        
        response = courier.login_courier("wrong_login", courier_data["password"])
        assert response.status_code == 404
        assert response.json()["message"] == MSG['LOGIN_NOT_FOUND']
    
    
    @allure.title("Авторизация без обязательного поля логин")
    def test_login_courier_without_login_returns_error(self):
        response = courier.login_courier("", "any_password")
        assert response.status_code == 400
        assert response.json()["message"] == MSG['LOGIN_NO_DATA']
    
    @allure.title("Авторизация без обязательного поля пароль")
    def test_login_courier_without_password_returns_error(self):
        response = courier.login_courier("any_login", "")
        
        assert response.status_code == 400
        assert response.json()["message"] == MSG['LOGIN_NO_DATA']
    
    @allure.title("Авторизация под несуществующим пользователем")
    def test_login_courier_with_nonexistent_credentials_returns_error(self):
        response = courier.login_courier(
        "nonexistent_" + DataGenerator.generate_random_string(10),
        "any_password"
          )
        assert response.status_code == 404
        assert response.json()["message"] == MSG['LOGIN_NOT_FOUND']