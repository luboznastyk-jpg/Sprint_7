BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1"

ENDPOINTS = {
    "courier": "/courier",
    "courier_login": "/courier/login",
    "courier_delete": "/courier/{id}",
    "orders": "/orders",
    "orders_cancel": "/orders/cancel"
}

MSG = {
    'COURIER_CREATE_NO_DATA': 'Недостаточно данных для создания учетной записи',
    'COURIER_DUPLICATE_LOGIN': 'Этот логин уже используется. Попробуйте другой.',

    'COURIER_DELETE_NO_ID': 'Недостаточно данных для удаления курьера',
    'COURIER_DELETE_NOT_FOUND': 'Курьера с таким id нет.',
    'NOT_FOUND': 'Not Found.',
    

    'LOGIN_NO_DATA': 'Недостаточно данных для входа',
    'LOGIN_NOT_FOUND': 'Учетная запись не найдена',

    'ORDER_ACCEPT_NO_DATA': 'Недостаточно данных для поиска',
    'ORDER_ACCEPT_NOT_FOUND': 'Заказа с таким id не существует',
    'ORDER_ACCEPT_COURIER_NOT_FOUND': 'Курьера с таким id не существует',
    'ORDER_ALREADY_IN_WORK': 'Этот заказ уже в работе',

    'ORDER_TRACK_NO_DATA': 'Недостаточно данных для поиска',
    'ORDER_TRACK_NOT_FOUND': 'Заказ не найден',
    'ORDERS_LIST_COURIER_NOT_FOUND_START': 'Курьер с идентификатором',
    'ORDERS_LIST_COURIER_NOT_FOUND_END': 'не найден',
}