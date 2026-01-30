#  Sprint_7
https://qa-scooter.praktikum-services.ru/


Проект содержит автотесты API сервиса Яндекс Самокат. 
Покрыты ручки API для работы с курьерами и заказами.

#  Документация API
https://qa-scooter.praktikum-services.ru/docs/


# Тестовые сценарии
1. Проверки создания курьера test_create_courier.py:
Проверка успешного создания курьера - test_create_courier_success_shows_ok_true
Проверка, что нельзя создать двух одинаковых курьеров - test_create_duplicate_courier_shows_error
Проверка создания курьера без обязательного поля - test_create_courier_missing_field_shows_error 

2. Проверки авторизации курьера test_login_courier.py:
Курьер может авторизоваться - test_login_courier_with_valid_credentials_returns_id
Если неправильно указать логин или пароль, запрос возвращает ошибку  - test_login_courier_with_wrong_password_returns_error
Авторизация под несуществующим пользователем, запрос возвращает ошибку - test_login_courier_with_nonexistent_credentials_returns_error
Если какого-то поля нет, запрос возвращает ошибку - test_login_courier_missing_field_returns_error 

3. Проверки создания заказа test_create_order.py:
Проверка создания заказа с одним из двух цветов - test_create_order_with_different_colors_returns_track
Проверка создания заказа: указать два цвета - test_create_order_with_different_colors_returns_track
Проверка создания заказа: не указывать цвет (пустой массив) - test_create_order_with_different_colors_returns_track
Проверка создания заказа: не указывать цвет (отсутствие поля) - test_create_order_without_color_field_returns_track

4. Проверки получения списка заказов test_get_orders_list.py:
В тело ответа возвращается список заказов - test_get_orders_base
Получить все активные/завершенные заказы курьера - test_get_orders_with_courier_id
Получить все  активные/завершенные заказы курьера на станциях '1' или '2' - test_get_orders_with_courier_id_and_stations
Получить  10 заказов, доступных для взятия курьером - test_get_10_orders
Получить  10 заказов, доступных для взятия курьером возле метро 'Калужская' - test_get_10_orders_near_station_110