import allure
from methods import ScooterMethods


class TestGetOrdersList:
    
    @allure.title("Тест: запрос возвращает список заказов")
    def test_get_orders_list(self, create_and_cancel_order):
        order = ScooterMethods()
        response = order.get_orders_list()
        assert response.status_code == 200
        assert "orders" in response.json()
            