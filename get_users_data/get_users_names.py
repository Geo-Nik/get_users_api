import requests
import logging

TUPLE_OF_PAGES_NUMBERS = (1, 2)
API_URL_TEMPLATE = "https://reqres.in/api/users?page={}"
USER_DATA_DICT_KEYWORD = "data"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    "AppleWebKit/537.36 (KHTML, like Gecko)"
    "Chrome/67.0.3396.79 Safari/537.36",
}


def get_api_url(page):
    return API_URL_TEMPLATE.format(page)


def get_response(page):
    api_url = get_api_url(page)
    try:
        response = requests.get(api_url, headers=HEADERS)
        return response
    except requests.exceptions.InvalidSchema as err:
        logging.error(f"The url is invalid: {err}")
    except requests.exceptions.ConnectionError as err:
        logging.error(f"The connection is invalid: {err}")


def get_data(page):
    response = get_response(page)
    if response:
        return response.json()


def get_user_data(page):
    data = get_data(page)
    if data:
        return data[USER_DATA_DICT_KEYWORD]


def get_user_data_from_all_pages():
    user_data_all_pages = []
    for page in TUPLE_OF_PAGES_NUMBERS:
        user_data_all_pages.extend(get_user_data(page))
    return user_data_all_pages


def is_ids_range_valid(ids_range):
    if len(ids_range) > 2:
        return False
    elif not isinstance(ids_range[0], int) or not isinstance(ids_range[1], int):
        return False
    elif ids_range[1] - ids_range[0] < 0:
        return False
    elif ids_range[1] <= 0 or ids_range[0] <= 0:
        return False
    return True


def is_user_id_in_range(ids_range):
    return lambda user_data_dict: ids_range[0] <= user_data_dict["id"] <= ids_range[1]


def filter_users_data_by_id(ids_range):
    user_data_list = get_user_data_from_all_pages()
    if is_ids_range_valid(ids_range):
        return list(filter(is_user_id_in_range(ids_range), user_data_list))
    empty_list = []
    return empty_list


def generate_full_name(user_data_dict):
    return f"{user_data_dict['first_name']} {user_data_dict['last_name']}"


def get_user_full_name_list(start_of_range, end_of_range):
    ids_range = (start_of_range, end_of_range)
    filtered_data = filter_users_data_by_id(ids_range)
    list_of_names = list(map(generate_full_name, filtered_data))
    list_of_names.sort()
    return list_of_names


if __name__ == "__main__":
    IDs_RANGE = (1, 3)
    list_of_names = get_user_full_name_list(*IDs_RANGE)
    print(list_of_names)
    # --------------------------------------------------
    IDs_RANGE = (5, 8)
    list_of_names = get_user_full_name_list(*IDs_RANGE)
    print(list_of_names)
