import pytest
import allure

from data import TestOrderData
from api_yandex_samokat import ApiYandexSamokat


class TestCreatingOrder:

    @allure.title('Проверка успешного создания заказа с разными данными')
    @allure.description('Отправляем запрос, проверяем,что код ответа 201 и в сообщении присуствует номер заказа track - позитивный сценарий')
    @pytest.mark.parametrize('order_body', [TestOrderData.ORDER_BODY_BLACK, TestOrderData.ORDER_BODY_GREY, TestOrderData.ORDER_BODY_BLACK_GREY, TestOrderData.ORDER_BODY_NO_COLOUR])
    def test_successful_create_order_code(self, order_body, cancel_order_fixture):
        order_request = ApiYandexSamokat.create_order(order_body)
        order_track = order_request.json()['track']
        cancel_order_fixture['track'] = order_track

        assert order_request.status_code == 201
        assert order_request.json()['track'] != ""
