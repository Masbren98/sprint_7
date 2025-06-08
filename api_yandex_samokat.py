import requests
import urls
import allure


class ApiYandexSamokat:

    @allure.step('Создание нового курьера')
    def creation_courier(body):
        return requests.post(urls.CREATING_COURIER_URL, data=body)

    @allure.step('Авторизация курьера')
    def login_courier(body):
        return requests.post(urls.LOGIN_COURIER_URL, data=body)

    @allure.step('Создание нового заказа')
    def create_order(body):
        return requests.post(urls.CREATE_ORDER_URL, json=body)

    @allure.step('Получение списка всех заказов')
    def get_list_orders():
        return requests.get(urls.GET_LIST_ORDERS_URL)

    @allure.step('Отмена заказа по номеру track')
    def cancel_order(order_track):
        return requests.put(f"{urls.CANCEL_ORDER_URL}?track={order_track}")

    @allure.step('Удаление курьера по id')
    def delete_courier(courier_id):
        return requests.delete(f"{urls.DELETE_COURIER_URL}{courier_id}")
