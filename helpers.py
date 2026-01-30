import string
import random
from datetime import datetime, timedelta

class DataGenerator:
    @staticmethod
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def generate_courier_data():
        return {
            "login": DataGenerator.generate_random_string(10),
            "password": DataGenerator.generate_random_string(10),
            "firstName": DataGenerator.generate_random_string(10)
        }

    @staticmethod
    def generate_order_data():
        return {
            "firstName": DataGenerator.generate_random_string(10),
            "lastName": DataGenerator.generate_random_string(10),
            "address": DataGenerator.generate_random_string(10),
            "metroStation": random.randint(1, 10),
            "phone": f"+7{random.randint(9000000000, 9999999999)}",
            "rentTime": random.randint(1, 7),
            "deliveryDate": (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d"),
            "comment": " "
        }


