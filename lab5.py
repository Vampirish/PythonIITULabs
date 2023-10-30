from datetime import datetime


def get_keys_with_value_true(dicti):
    return [k for k, v in dicti.items() if v]


def get_unique_elements(listi):
    return [i for i in listi if listi.count(i) == 1]


def get_date_in_format(date):
    dateUpd = date.split('.')
    return f"{dateUpd[2]}.{dateUpd[1]}.{dateUpd[0]}"


def get_elements_with_no_more_than_two_occurrences(listi):
    return [i for i in listi if listi.count(i) <= 2]


def get_words_from_string(string):
    return string.split()


def get_unique_elements_with_count(listi):
    d = {}
    for i in listi:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def get_prime_numbers(n):
    listi = []
    for i in range(2, n):
        check = True
        for j in listi:
            if i % j == 0:
                check = False
        if check:
            listi.append(i)
    return listi


def get_prime_numbers_in_list(listi):
    mx = max(listi)
    primeNumbers = get_prime_numbers(mx)
    return [i for i in listi if i in primeNumbers]


def get_difference_between_dates(date1, date2):
    form = "%Y.%m.%d"
    date1 = datetime.strptime(date1, form)
    date2 = datetime.strptime(date2, form)
    return (date2 - date1).days


def get_decimal_number_from_binary_string(binary_string):
    return int(binary_string, 2)


def get_perfect_squares(listi):
    listAns = []
    for i in listi:
        if int(i ** 0.5) ** 2 == i:
            listAns.append(i)
    return listAns


def sort_by_price(shopping_list):
    return sorted(shopping_list, key=lambda x: x['price'])


def get_words_starting_with_vowel(words):
    vow = "aoieu"
    return [i for i in words if i[0].lower() in vow]


def main():
    print("\nTask 1.1")
    dicti = {
        "a": True,
        "b": False,
        "c": True
    }
    print(get_keys_with_value_true(dicti))

    print("\nTask 1.2")
    listi = [1, 2, 3, 1, 2, 4]
    print(get_unique_elements(listi))

    print("\nTask 1.3")
    date = "2023.10.23"
    print(get_date_in_format(date))

    print("\nTask 1.4")
    listi = [1, 2, 3, 1, 2, 4, 1, 2]
    print(get_unique_elements(listi))

    print("\nTask 1.5")
    string = "This a string with a several words."
    print(get_words_from_string(string))

    print("\nTask 2.6")
    listi = [1, 2, 3, 1, 2, 4, 1, 2]
    print(get_unique_elements_with_count(listi))

    print("\nTask 2.7")
    n = 100
    print(get_prime_numbers(n))

    print("\nTask 2.8")
    listi = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]
    print(get_prime_numbers_in_list(listi))

    print("\nTask 2.9")
    date1 = "2023.10.23"
    date2 = "2023.10.24"
    print(get_difference_between_dates(date1, date2))

    print("\nTask 2.10")
    b = "10110011"
    print(get_decimal_number_from_binary_string(b))

    print("\nTask 2.11")
    listi = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(get_perfect_squares(listi))

    print("\nTask 2.12")
    shopping_list = [
        {"name": "Apple", "price": 100},
        {"name": "Banana", "price": 50},
        {"name": "Orange", "price": 20}
    ]
    print(sort_by_price(shopping_list))

    print("\nTask 2.13")
    words = ["apple", "banana", "orange", "bear", "cat"]
    print(get_words_starting_with_vowel(words))


main()