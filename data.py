
class TestAuthorizationData:
    REGISTRATION_COURIER_BODY = {
        "login": "qwerty",
        "password": "12345",
        "firstName": "qwe"
    }

    REGISTRATION_COURIER_BODY_EMPTY_LOGIN = {
        "login": "",
        "password": "12345",
        "firstName": "qwe"
    }

    REGISTRATION_COURIER_BODY_EMPTY_PASSWORD = {
        "login": "qwerty",
        "password": "",
        "firstName": "qwe"
    }

    REGISTRATION_COURIER_BODY_EMPTY_FIRSTNAME = {
        "login": "qwerty13",
        "password": "12345",
        "firstName": ""
    }

    REGISTRATION_COURIER_BODY_NOT_ALL_FIELDS = {
        "login": "qwerty1313",
        "password": "12345"
    }

    LOGIN_COURIER_BODY_NOT_EXISTED = {
            "login": "kfkfkfkf",
            "password": "00000"
        }

    LOGIN_COURIER_BODY_EMPTY_LOGIN = {
            "login": "",
            "password": "11111"
        }

    LOGIN_COURIER_BODY_EMPTY_PASSWORD = {
            "login": "kfkfkfkf",
            "password": ""
        }

    LOGIN_COURIER_BODY_NOT_ALL_FIELDS = {
        "password": ""
    }


class TestOrderData:

    ORDER_BODY_BLACK = {
        "firstName": "Мария",
        "lastName": "Иванова",
        "address": "Охотный ряд",
        "metroStation": 4,
        "phone": "+7 912 111 11 11",
        "rentTime": 5,
        "deliveryDate": "2025-05-14",
        "comment": "нет",
        "color": ["BLACK"]}

    ORDER_BODY_GREY = {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "улица Ленина",
        "metroStation": 7,
        "phone": "+7 911 222 22 22",
        "rentTime": 3,
        "deliveryDate": "2025-05-20",
        "comment": "Скорее",
        "color": ["GREY"]}

    ORDER_BODY_NO_COLOUR = {
        "firstName": "Данила",
        "lastName": "Иванов",
        "address": "улица Строителей",
        "metroStation": 7,
        "phone": "+7 921 333 33 33",
        "rentTime": 3,
        "deliveryDate": "2025-05-25",
        "comment": "Люблю самокаты",
        "color": []}

    ORDER_BODY_BLACK_GREY = {
        "firstName": "Олег",
        "lastName": "Иванов",
        "address": "проспект Мира",
        "metroStation": 2,
        "phone": "+7 911 444 44 44",
        "rentTime": 1,
        "deliveryDate": "2025-05-27",
        "comment": "Яндекс супер",
        "color": ["BLACK", "GREY"]}
