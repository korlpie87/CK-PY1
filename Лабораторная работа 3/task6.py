list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0

for i, current_number in enumerate(list_numbers):  # перебираем все пары индекс-значение
    max_number = list_numbers[max_index]
    if current_number >= max_number:
        max_index = i  # перезаписываем индекс максимального элемента
        max_number = list_numbers[max_index]  # перезаписываем максимальное число

# присвоим найденному максимальному и последнему элементу имена переменных:
list_numbers[9], list_numbers[-1] = list_numbers[-1], list_numbers[9]

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
