import requests
import allure
from data import BASE_URL, ENDPOINTS

class ScooterMethods:
    def __init__(self):
        self.base_url = BASE_URL
        self.endpoints = ENDPOINTS
    
    @allure.step("Создание курьера")
    def create_courier(self, courier_data):
        response = requests.post(
            f'{self.base_url}{self.endpoints["courier"]}', verify=False,

        data=courier_data,
        )
        return response

    @allure.step("Авторизация курьера")
    def login_courier(self, login, password):
        response = requests.post(
            f'{self.base_url}{self.endpoints["courier_login"]}', verify=False,
            data={"login": login, "password": password}
        )
        return response

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        requests.delete(
            f'{self.base_url}{self.endpoints["courier_delete"]}'.format(id=courier_id), verify=False
        )

    @allure.step("Создание заказа")
    def create_order(self, order_data):
        response = requests.post(
            f'{self.base_url}{self.endpoints["orders"]}', verify=False,
            json=order_data
        )
        return response

    @allure.step("Отмена заказа")
    def cancel_order(self, track):
        response = requests.put(
            f'{self.base_url}{self.endpoints["orders_cancel"]}', verify=False,
            params={"track": track}
        )
        return response

    @allure.step("Получение списка заказов")
    def get_orders_list(self, params=None):
        return requests.get(
            f'{self.base_url}{self.endpoints["orders"]}', verify=False,
        params=params)
  
courier = ScooterMethods()