"""" Reviews"""

import json


def import_file(file):
    with open(file) as f:
        input_file = f.readlines()
    return [json.loads(line) for line in input_file]


def import_from_json():
    """Imports a json file and converts it to python
    """
    business_data = import_file('business_data.txt')
    user_data = import_file('user_data.txt')
    review_data = import_file('review_data.txt')
    return business_data, user_data, review_data


def return_reviews_for_business(reviews_data, company_name):
    reviews_list = [review for review in reviews_data if company_name == review['business_name']]
    return reviews_list


def main():
    business_data, user_data, review_data = import_from_json()
    return_reviews_for_business(review_data, 'Voodoo Donuts')
    # return_average_business_rating()
    # return_users_review()
    # return_city_review_average()


if __name__ == '__main__':
    main()