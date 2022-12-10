import random


def get_unique_list_numbers() -> list[int]:
    start = -10
    stop = 11
    k = 15

    list_numbers = random.sample([i for i in range(start, stop)], k)
    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
                    # конец кода