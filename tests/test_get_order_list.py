import allure
from methods import courier


class TestGetOrdersList:
    
    @allure.title("Тест: запрос возвращает список заказов")
    def test_get_orders_list(self):
        response = courier.get_orders_list()
        assert response.status_code == 200
        assert "orders" in response.json()
            