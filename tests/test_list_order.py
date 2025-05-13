import allure

from data import TestOrderData
from api_yandex_samokat import ApiYandexSamokat


class TestGetListOrders:

    @allure.title('Проверка успешного получения списка всех заказов')
    @allure.description('Отправляем запрос, проверяем,что код ответа 200 и в сообщении список закозов')
    def test_successful_get_list_orders_code(self):

        order_request = ApiYandexSamokat.create_order(TestOrderData.ORDER_BODY_BLACK)
        order_track1 = order_request.json()['track']
        order_request = ApiYandexSamokat.create_order(TestOrderData.ORDER_BODY_GREY)
        order_track2 = order_request.json()['track']
        order_request = ApiYandexSamokat.create_order(TestOrderData.ORDER_BODY_NO_COLOUR)
        order_track3 = order_request.json()['track']

        list_orders_request = ApiYandexSamokat.get_list_orders()

        assert list_orders_request.status_code == 200
        assert list_orders_request.json()['orders'] != []

        ApiYandexSamokat.cancel_order(order_track1)
        ApiYandexSamokat.cancel_order(order_track2)
        ApiYandexSamokat.cancel_order(order_track3)
