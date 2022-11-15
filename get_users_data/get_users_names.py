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
    """
    get_api_url generates api url using API_URL_TEMPLATE and page number
    :param page: the number of API page: int
    :return : API url: str

    """
    return API_URL_TEMPLATE.format(page)


def get_response(page):
    """
    get_response gets get response from API
    :param page: the number of API page: int
    :return : requests.get response in case no error and None in case any error
    """
    api_url = get_api_url(page)
    try:
        response = requests.get(api_url, headers=HEADERS)
        return response
    except requests.exceptions.InvalidSchema as err:
        logging.error(f"The url is invalid: {err}")
    except requests.exceptions.ConnectionError as err:
        logging.error(f"The connection is invalid: {err}")


def get_data(page):
    """
    get_data gets data for specified page from target API
    :param page: the number of API page: int
    :return : API data as a dict if response exists or None
    if response does not exists
    :example: {"page":1,"per_page":3,"total":12,"total_pages":4,
    "data": [{"id":1,"first_name":"George","last_name":"Bluth",
    "avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg"} ... ]
    """
    response = get_response(page)
    if response:
        return response.json()


def get_user_data(page):
    """
    get_user_data gets list of user data from the dict by USER_DATA_DICT_KEYWORD
    :param page: the number of API page: int
    :return : list of user data
    :example: [{"id":1,"first_name":"George","last_name":"Bluth",
    "avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg"} ... ]
    """
    data = get_data(page)
    if data:
        return data[USER_DATA_DICT_KEYWORD]


def get_user_data_from_all_pages():
    """
    get_user_data_from_all_pages gets lists of user data from all pages in TUPLE_OF_PAGES_NUMBERS
    and join them in the only list
    :return : joined list of user data
    :example: [{"id":1,"first_name":"George","last_name":"Bluth",
    "avatar":"https://s3.amazonaws.com/uifaces/faces/twitter/calebogden/128.jpg"} ... ]
    """
    user_data_all_pages = []
    for page in TUPLE_OF_PAGES_NUMBERS:
        user_data_all_pages.extend(get_user_data(page))
    return user_data_all_pages


def is_ids_range_valid(ids_range):
    """
    is_ids_range_valid checks if range contains only two integer positive values
    and end of range is greater than start of range
    :param ids_range: range specified by user for filtering ids according to requirements: tuple
    return: True or False
    """
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
    """
    is_user_id_in_range checks if user id is in ids_range
    :param ids_range: range specified by user for filtering ids according to requirements: tuple
    :param user_data_dict: dictionary with data for one user
    return True or False
    """
    return lambda user_data_dict: ids_range[0] <= user_data_dict["id"] <= ids_range[1]


def filter_users_data_by_id(ids_range):
    """
    filter_users_data_by_id filters all users by id (id should be in the ids_range including ends of range)
    :param ids_range: range specified by user for filtering ids according to requirements: tuple
    return filtered list if ids_range is valid and empty list if ids_range is invalid
    """
    user_data_list = get_user_data_from_all_pages()
    if is_ids_range_valid(ids_range):
        return list(filter(is_user_id_in_range(ids_range), user_data_list))
    empty_list = []
    return empty_list


def generate_full_name(user_data_dict):
    """
    generate_full_name creates string with user full name according to data from user_data_dict
    :param user_data_dict: dictionary with user data
    return user full name: str
    """
    return f"{user_data_dict['first_name']} {user_data_dict['last_name']}"


def get_user_full_name_list(start_of_range, end_of_range):
    """
    get_user_full_name_list gets sorted by first name list of users full name which ids are in specified range
    :param start_of_range: start of range defined by user: int
    :param end_of_range: end of range defined by user: int
    return sorted list of full users name
    """
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
