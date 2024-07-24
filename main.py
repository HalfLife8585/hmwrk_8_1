def add_one(some_list):
    # Перетворюємо список цифр на число
    number = 0
    for digit in some_list:
        number = number * 10 + digit

    # Додаємо 1
    number += 1

    # Перетворюємо число назад у список цифр
    result = []
    while number > 0:
        result.insert(0, number % 10)
        number //= 10

    # Якщо вхідний список був [0], повертаємо [1]
    return result if result else [1]

