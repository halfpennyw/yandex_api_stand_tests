import configuration
import requests
import data

# Определяем функцию get_logs, которая не принимает параметров
def get_logs():
    return requests.get(configuration.URL_SERVICE+configuration.LOG_MAIN_PATH, params={"count":20})

# response = get_logs()
# print(response.status_code)
# print(response.headers)

# Определяем функцию get_users_table, которая не принимает параметров
def get_users_table():
    return requests.get(configuration.URL_SERVICE+configuration.USERS_TABLE_PATH)

# response = get_users_table()
# print(response.status_code)
# print(response.text)

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):

    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
# response = post_new_user(data.user_body);
#
# print(response.status_code)
# print(response.json())

def post_products_kits(products_ids):

    return  requests.post(configuration.URL_SERVICE+configuration.PRODUCTS_KITS_PATH,
                          json=products_ids,
                          headers=data.headers)

# Вызов функции post_products_kits с телом запроса для создания нового пользователя из модуля data
response = post_products_kits(data.product_ids)

print(response.status_code)
print(response.json())