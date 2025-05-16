import allure

from helper import DataHelper
from api_yandex_samokat import ApiYandexSamokat
from data import AuthorizationData


class TestCreatingCourier:

    @allure.title('Проверка успешного создания нового курьера')
    @allure.description('Отправляем запрос, проверяем,что код ответа 201 и тело ответа {"ok":True}')
    def test_successful_creating_courier_correct_answer(self):
        body = DataHelper.generate_registration_body()
        registration_request = ApiYandexSamokat.creation_courier(body)
        login_request = ApiYandexSamokat.login_courier(DataHelper.generate_login_courier_body(body))
        courier_id = login_request.json().get('id')

        assert registration_request.status_code == 201
        assert registration_request.json().get('ok') is True
        assert courier_id is not None
        ApiYandexSamokat.delete_courier(courier_id)

    @allure.title('Проверка ошибки регистрации нового курьера с уже существующим логином')
    @allure.description('Отправляем запрос, проверяем,что код ответа 409 и текст ошибки {"message":"Этот логин уже используется"}')
    def test_failed_creating_existing_courier(self, new_couriers_and_clear_courier_data):
        body = new_couriers_and_clear_courier_data['data']
        registration_request_double = ApiYandexSamokat.creation_courier(body)

        assert registration_request_double.status_code == 409
        assert (registration_request_double.json()["message"] == "Этот логин уже используется")

    @allure.title('Проверка ошибки регистрации нового курьера с пустым логином')
    @allure.description('Отправляем запрос, проверяем,что код ответа 400 и текст ошибки {"message":"Недостаточно данных для создания учетной записи"}')
    def test_failed_creating_courier_empty_login(self):
        registration_request = ApiYandexSamokat.creation_courier(AuthorizationData.REGISTRATION_COURIER_BODY_EMPTY_LOGIN)

        assert registration_request.status_code == 400
        assert registration_request.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка ошибки регистрации нового курьера с пустым паролем')
    @allure.description('Отправляем запрос, проверяем,что код ответа 400 и текст ошибки {"message":"Недостаточно данных для создания учетной записи"}')
    def test_failed_registration_courier_empty_password_error_code(self):
        registration_request = ApiYandexSamokat.creation_courier(AuthorizationData.REGISTRATION_COURIER_BODY_EMPTY_PASSWORD)

        assert registration_request.status_code == 400
        assert registration_request.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Проверка ошибки регистрации нового курьера с пустым именем')
    @allure.description('Отправляем запрос, проверяем,что код ответа не 201')
    def test_failed_registration_courier_empty_firstname_error_code(self):
        registration_request = ApiYandexSamokat.creation_courier(AuthorizationData.REGISTRATION_COURIER_BODY_EMPTY_FIRSTNAME)

        assert registration_request.status_code != 201

    @allure.title('Проверка ошибки регистрации нового курьера при незаполнении всех обязательных полей')
    @allure.description('Отправляем запрос, проверяем,что код ответа не 201')
    def test_failed_registration_courier_not_all_fields(self):
        registration_request = ApiYandexSamokat.creation_courier(AuthorizationData.REGISTRATION_COURIER_BODY_NOT_ALL_FIELDS)

        assert registration_request.status_code != 201
