import allure

from data import TestAuthorizationData
from helper import TestDataHelper
from api_yandex_samokat import ApiYandexSamokat


class TestLoginCourier:

    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Отправляем запрос, проверяем,что код ответа 200 и в ответе есть id курьера')
    def test_successful_login_courier(self, new_couriers_and_clear_courier_data):
        body = new_couriers_and_clear_courier_data['data']
        login_request = ApiYandexSamokat.login_courier(body)
        courier_id = login_request.json().get('id')

        assert login_request.status_code == 200
        assert courier_id is not None

    @allure.title('Проверка ошибки авторизации курьера с ошибкой в логине')
    @allure.description('Отправляем запрос, проверяем,что код ответа 404 и текст ошибки "Учетная запись не найдена"')
    def test_failed_mistake_login_courier(self, new_couriers_and_clear_courier_data):
        body = new_couriers_and_clear_courier_data['data']
        login_request = ApiYandexSamokat.login_courier(TestDataHelper.generate_mistake_login_courier_body(body))

        assert login_request.status_code == 404
        assert login_request.json()['message'] == "Учетная запись не найдена"

    @allure.title('Проверка ошибки авторизации курьера с ошибкой в пароле')
    @allure.description('Отправляем запрос, проверяем,что код ответа 404 и текст ошибки "Учетная запись не найдена"')
    def test_failed_mistake_password_courier(self, new_couriers_and_clear_courier_data):
        body = new_couriers_and_clear_courier_data['data']
        login_request = ApiYandexSamokat.login_courier(TestDataHelper.generate_mistake_password_courier_body(body))

        assert login_request.status_code == 404
        assert login_request.json()['message'] == "Учетная запись не найдена"

    @allure.title('Проверка ошибки авторизации несуществующего курьера')
    @allure.description('Отправляем запрос, проверяем,что код ответа 404 и текст ошибки "Учетная запись не найдена"')
    def test_failed_login_courier_not_existed(self):
        login_request = ApiYandexSamokat.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_NOT_EXISTED)

        assert login_request.status_code == 404
        assert login_request.json()['message'] == "Учетная запись не найдена"

    @allure.title('Проверка ошибки авторизации курьера без логина')
    @allure.description('Отправляем запрос, проверяем,что код ответа 400 и текст ошибки "Недостаточно данных для входа"')
    def test_failed_login_courier_empty_login(self):
        login_request = ApiYandexSamokat.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_EMPTY_LOGIN)

        assert login_request.status_code == 400
        assert login_request.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Проверка ошибки авторизации курьера без пароля')
    @allure.description('Отправляем запрос, проверяем,что код ответа 400 и текст ошибки "Недостаточно данных для входа"')
    def test_failed_login_courier_empty_password(self):
        login_request = ApiYandexSamokat.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_EMPTY_PASSWORD)

        assert login_request.status_code == 400
        assert login_request.json()['message'] == "Недостаточно данных для входа"

    @allure.title('Проверка ошибки авторизации курьера при незаполнении всех обязательных полей')
    @allure.description('Отправляем запрос, проверяем,что код ответа не 201')
    def test_failed_login_courier_not_all_fields(self):
        login_request = ApiYandexSamokat.login_courier(TestAuthorizationData.LOGIN_COURIER_BODY_NOT_ALL_FIELDS)

        assert login_request.status_code != 201
